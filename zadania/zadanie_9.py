import qgis.core

path = os.path.join(os.path.expanduser("~"), "Documents", "dane")
os.chdir(path)

file = "powiaty.gpkg"
vector = QgsVectorLayer(file)

geometry_type = "Point"
crs = "EPSG:2180"

centroids = QgsVectorLayer(geometry_type+"?crs="+crs, "Centroidy", "memory")
centroids_provider = centroids.dataProvider()

centroids.startEditing()
for feature in vector.getFeatures():
    geom = feature.geometry()
    centroid = QgsFeature()
    centroid.setGeometry(geom.centroid())
    centroids_provider.addFeature(centroid)

centroids.updateExtents()
centroids.commitChanges()

options = QgsVectorFileWriter.SaveVectorOptions()
options.driverName = "gpkg"
options.fileEncoding = "UTF-8"
options.layerName = "centroidy"
write = QgsVectorFileWriter. \
    writeAsVectorFormatV3(centroids, "powiaty_centroidy.gpkg",QgsCoordinateTransformContext(), options) 
