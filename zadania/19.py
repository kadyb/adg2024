from qgis.core import (
    QgsProcessing,
    QgsProcessingAlgorithm,
    QgsProcessingParameterFeatureSource,
    QgsProcessingParameterFeatureSink,
    QgsProcessingException,
    QgsWkbTypes,
    QgsField,
    QgsFeature
)
from qgis.PyQt.QtCore import QVariant


class ConvertCoordinatesToDMS(QgsProcessingAlgorithm):
    
    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'

    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                'Input layer',
                [QgsProcessing.TypeVectorPoint]
            )
        )
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT,
                'Output layer'
            )
        )

    def degrees_to_dms(self, coord, coord_type):
        direction = ''
        if coord_type == 'lat':
            direction = 'N' if coord >= 0 else 'S'
        elif coord_type == 'lon':
            direction = 'E' if coord >= 0 else 'W'

        coord = abs(coord)
        degrees = int(coord)
        minutes = int((coord - degrees) * 60)
        seconds = round((coord - degrees - minutes / 60) * 3600, 2)

        return f"{degrees}\u00b0{minutes}'{seconds}\"{direction}"

    def processAlgorithm(self, parameters, context, feedback):
        source = self.parameterAsSource(parameters, self.INPUT, context)
        if source is None:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.INPUT))

        fields = source.fields()
        fields.append(QgsField('Lat_DMS', QVariant.String))
        fields.append(QgsField('Lon_DMS', QVariant.String))

        (sink, dest_id) = self.parameterAsSink(
            parameters,
            self.OUTPUT,
            context,
            fields,
            source.wkbType(),
            source.sourceCrs()
        )

        for feature in source.getFeatures():
            geom = feature.geometry()
            if geom.isEmpty():
                continue

            if geom.type() == QgsWkbTypes.PointGeometry:
                point = geom.asPoint()
                lat_dms = self.degrees_to_dms(point.y(), 'lat')
                lon_dms = self.degrees_to_dms(point.x(), 'lon')

                new_feature = QgsFeature(fields)
                new_feature.setGeometry(geom)
                new_feature.setAttributes(feature.attributes() + [lat_dms, lon_dms])
                sink.addFeature(new_feature)

        return {self.OUTPUT: dest_id}

    def name(self):
        return 'convert_coords_to_dms'

    def displayName(self):
        return 'Convert Coordinates to DMS'

    def group(self):
        return 'Custom Scripts'

    def groupId(self):
        return 'customscripts'

    def createInstance(self):
        return ConvertCoordinatesToDMS()
