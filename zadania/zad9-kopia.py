'''
Stwórz nową warstwę z obliczonymi centroidami dla powiatów i zapisz ją na
dysku w formacie .gpkg.
'''
import qgis.core
from qgis.core import QgsVectorLayer, QgsFeature, QgsVectorFileWriter, QgsCoordinateTransformContext
import os

data_folder = "/Users/michalbaczkiewicz/Documents/GitHub/adg2024/dane/"
os.chdir(data_folder)
input_file = "powiaty.gpkg"
source_layer = QgsVectorLayer(input_file, "powiaty", "ogr")

target_geometry_type = "Point"
coordinate_system = source_layer.crs().toWkt()
centroid_layer = QgsVectorLayer(target_geometry_type + "?crs=" + coordinate_system, "Centroidy", "memory")
centroid_data_provider = centroid_layer.dataProvider()

centroid_data_provider.addAttributes(source_layer.fields())
centroid_layer.updateFields()
centroid_layer.startEditing()

for feature_item in source_layer.getFeatures():
    geometry_obj = feature_item.geometry()
    centroid_point = geometry_obj.centroid()
    new_feature_obj = QgsFeature()
    new_feature_obj.setGeometry(centroid_point)
    new_feature_obj.setAttributes(feature_item.attributes())
    centroid_data_provider.addFeature(new_feature_obj)
centroid_layer.updateExtents()
centroid_layer.commitChanges()

output_options = QgsVectorFileWriter.SaveVectorOptions()
output_options.driverName = "gpkg"
output_options.fileEncoding = "UTF-8"
output_options.layerName = "centroidy"

output_file_path = "powiaty_centroidy.gpkg"
write_result = QgsVectorFileWriter.writeAsVectorFormatV3(centroid_layer, output_file_path, QgsCoordinateTransformContext(), output_options)

if write_result[0] == QgsVectorFileWriter.WriterError.NoError:
    print(f"Warstwa centroidów została zapisana do: {output_file_path}")
else:
    print(f"Błąd podczas zapisu warstwy centroidów: {write_result[0]}")
