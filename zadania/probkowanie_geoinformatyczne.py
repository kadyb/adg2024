import random
from qgis.core import QgsPoint, QgsFeature, QgsVectorLayer, QgsField, QgsGeometry, QgsCoordinateReferenceSystem, QgsVectorFileWriter
from PyQt5.QtCore import QVariant

def sample_strata(vector, noOfPoints):
    pointsLayer = QgsVectorLayer('Point?crs=EPSG:2180', 'Losowane Punkty', 'memory')
    pointsLayerData = pointsLayer.dataProvider()
    
    idField = QgsField("id", QVariant.Int)
    pointsLayerData.addAttributes([idField])
    pointsLayer.updateFields()

    for feature in vector.getFeatures():
        polygonGeom = feature.geometry()
        
        if polygonGeom.area() > 0:
            for i in range(noOfPoints):
                point = randomPointInPolygon(polygonGeom)
                
                if point:
                    newPointFeature = QgsFeature()
                    newPointFeature.setGeometry(point)
                    newPointFeature.setAttributes([feature.id()])
                    pointsLayerData.addFeature(newPointFeature)
    
    return pointsLayer

def randomPointInPolygon(polygon):
    attempts = 1000
    for i in range(attempts):
        x = random.uniform(polygon.boundingBox().xMinimum(), polygon.boundingBox().xMaximum())
        y = random.uniform(polygon.boundingBox().yMinimum(), polygon.boundingBox().yMaximum())
        point = QgsPointXY(x, y)
        
        if polygon.contains(point):
            return QgsGeometry.fromPointXY(point)
    
    return None
    
def saveLayer(layer, outputPath):
    sourceCrs = layer.crs()
    targetCrs = QgsCoordinateReferenceSystem("EPSG:2180")
    context = QgsProject.instance().transformContext()
    
    options = QgsVectorFileWriter.SaveVectorOptions()
    options.driverName = "GPKG"
    options.ct = QgsCoordinateTransform(sourceCrs, targetCrs, context)
    
    writer = QgsVectorFileWriter.writeAsVectorFormatV3(
        layer = layer,
        fileName = outputPath,
        transformContext = context,
        options = options,
    )
    
    if writer[0] != 0:
        print("Błąd zapisu!")
    else:
        print("Zapis udany")
        
def main():
    filePath = "C:/Users/tymon/OneDrive/Pulpit/Projects/Justyna/Algorytmy/Dane/powiaty.gpkg"
    outputPath = "C:/Users/tymon/OneDrive/Pulpit/Projects/Justyna/Algorytmy/Dane/losowane_punkty.gpkg"

    vector = QgsVectorLayer(filePath, "powiaty", "ogr")
    print(vector.featureCount())
    
    noOfPoints = 5
    sampledPoints = sample_strata(vector, noOfPoints)
    
    saveLayer(sampledPoints, outputPath)

main()