import qgis.core as q
import numpy as np

def calculateStatistics(layer, attributeName):
    values = []
    for feature in vector.getFeatures():
        values.append(feature[attributeName])
    
    statistics = {
        "mean" : np.mean(values),
        'std': np.std(values),
        'min': np.min(values),
        '25%': np.percentile(values, 25),
        '50%': np.percentile(values, 50),
        '75%': np.percentile(values, 75),
        'max': np.max(values)
    }
    
    return statistics
    
def addLengthAndAreaAttributes(layer):
    lengthField = QgsField("Długość w km", QVariant.Double)
    areaField = QgsField("Powierzchnia w km2", QVariant.Double)
    vector.dataProvider().addAttributes([lengthField, areaField])

    vector.updateFields()

    lengthIdx = vector.fields().indexOf("Długość w km")
    areaIdx = vector.fields().indexOf("Powierzchnia w km2")
        

    for feature in vector.getFeatures():
        attr = feature.attributes()
        geom = feature.geometry()
        
        length = geom.length() / 1000
        area = geom.area() / 1000**2

        updatedFeature = {lengthIdx : length, areaIdx : area}
        vector.dataProvider().changeAttributeValues({feature.id() : updatedFeature})
        
    vector.commitChanges()

def calculateCentroids(inputLayer):
    centroidsLayer = QgsVectorLayer('Point?crs=EPSG:2180', 'centroidyPowiatów', 'memory')
    
    idField = QgsField('id', QVariant.Int)
    centroidsLayer.dataProvider().addAttributes([idField])
    centroidsLayer.updateFields()
    
    for feature in inputLayer.getFeatures():
        centroid = feature.geometry().centroid()
        
        newCentroidFeature = QgsFeature()
        newCentroidFeature.setGeometry(centroid)
        newCentroidFeature.setAttributes([feature.id()])
        
        centroidsLayer.dataProvider().addFeatures([newCentroidFeature])
        
    return centroidsLayer
    
def saveLayer(layer, outputPath):
    
    sourceCrs = layer.crs()
    targetCrs = QgsCoordinateReferenceSystem("ESPG:2180")
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
    outputPath = "C:/Users/tymon/OneDrive/Pulpit/Projects/Justyna/Algorytmy/Dane/centroidy.gpkg"
    vector = q.QgsVectorLayer(filePath, "powiaty", "ogr")

    print(vector.featureCount())
    print(vector.fields().count())
    print(vector.fields().names())

    addLengthAndAreaAttributes(vector)
    
    lengthStats = calculateStatistics(vector, "Długość w km")
    areaStats = calculateStatistics(vector, "Powierzchnia w km2")
    
    print(lengthStats)
    print(areaStats)
    
    centroidsLayer = calculateCentroids(vector)
    for centroid, powiat in zip(centroidsLayer.getFeatures(), vector.getFeatures()):
        print(f"Centroida dla powiatu {powiat['JPT_NAZWA_']}: {centroid.geometry()}")
        
        
    saveLayer(centroidsLayer, outputPath)
    
main()
    
    



