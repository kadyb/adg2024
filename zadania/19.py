from qgis.processing import alg
from qgis.core import QgsVectorLayer, QgsFeature, QgsField, QgsProject
from qgis.PyQt.QtCore import QVariant

@alg(name="create_centroids", label="Centroid Generator (twoj ulubiony)",
     group="examplescripts", group_label="Example Scripts")
@alg.input(type=alg.VECTOR_LAYER, name="INPUT", label="Input Vector Layer")
@alg.output(type=alg.VECTOR_LAYER, name="OUTPUT", label="Output Centroids Layer")
@alg.output(type=alg.STRING, name="METADATA", label="Metadata")

def create_centroids(instance, parameters, context, feedback, inputs):
    """
    Twoj ulubiony generator centroidow w okolicy.
    """

    layer = instance.parameterAsVectorLayer(parameters, "INPUT", context)
    

    if not layer.isValid():
        feedback.reportError("Invalid input layer!")
        return {}


    typ_geom = "Point"
    crs = layer.crs().authid()
    centroid_layer = QgsVectorLayer(f"{typ_geom}?crs={crs}", "Centroidy", "memory")
    centroid_provider = centroid_layer.dataProvider()


    centroid_provider.addAttributes([QgsField("id", QVariant.Int)])
    centroid_layer.updateFields()


    centroid_layer.startEditing()
    for idx, obiekt in enumerate(layer.getFeatures()):
        centroid = QgsFeature()
        centroid.setGeometry(obiekt.geometry().centroid())
        centroid.setAttributes([idx])  # Ustawienie atrybutu "id"
        centroid_provider.addFeature(centroid)
    
    centroid_layer.updateExtents()
    centroid_layer.commitChanges()


    QgsProject.instance().addMapLayer(centroid_layer)


    metadata = {
        "Input Layer": {
            "Name": layer.name(),
            "Data Source": layer.dataProvider().dataSourceUri(),
            "Number of Features": layer.featureCount(),
            "Geometry Type": layer.geometryType(),
            "Extent": layer.extent().toString(precision=2),
            "CRS": layer.crs().authid()
        },
        "Output Centroids Layer": {
            "Name": centroid_layer.name(),
            "Number of Features": centroid_layer.featureCount(),
            "Geometry Type": centroid_layer.geometryType(),
            "Extent": centroid_layer.extent().toString(precision=2),
            "CRS": centroid_layer.crs().authid()
        }
    }

    if feedback.isCanceled():
        return {}

    return {"OUTPUT": centroid_layer, "METADATA": metadata}