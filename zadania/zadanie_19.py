from qgis.processing import alg
from qgis.core import QgsVectorLayer, QgsFeature, QgsVectorFileWriter, QgsPointXY, QgsGeometry
import random


@alg(name = "wektor_probkowanie", label = "Generowanie losowych punktow w poligonie",
     group = "przykladoweskrypty" , group_label = "Przykladowy skrypt")
@alg.input(type = alg.VECTOR_LAYER, name = "INPUT", label = "Wartwa wektorowa")
@alg.input(type = alg.INT, name = "LICZBA_PUNKTOW", label = "Licza punktow", default = 50)
@alg.input(type = alg.VECTOR_LAYER_DEST, name = "SCIEZKA_ZAPISU", label = "Sciezka zapisu")
@alg.output(type = alg.FILE, name = "OUTPUT", label = "Probkowanie")

def probkowanie(instance, parameters, context, feedback, inputs):
    """
    Probkowanie staryfikowane
    """
    
    layer = instance.parameterAsVectorLayer(parameters, "INPUT", context)
    liczba_punktow = instance.parameterAsInt(parameters, "LICZBA_PUNKTOW", context)
    sciezka_zapisu = instance.parameterAsOutputLayer(parameters, "SCIEZKA_ZAPISU", context)

    crs = layer.crs().authid()
    probkowanie_layer = QgsVectorLayer("Point?crs="+crs, "Probkowanie", "memory")
    
    if feedback.isCanceled():
        return {}

    probkowanie_layer.startEditing()
    # losowanie punktów
    for feat in layer.getFeatures():
        polygon = feat.geometry()
        bbox = polygon.boundingBox()
        punkty = 0
        while punkty < liczba_punktow:
            x = random.uniform(bbox.xMinimum(), bbox.xMaximum())
            y = random.uniform(bbox.yMinimum(), bbox.yMaximum())
            pt = QgsPointXY(x, y)
            if polygon.contains(pt):
                pnt = QgsGeometry.fromPointXY(pt)
                feature = QgsFeature()
                feature.setGeometry(pnt)
                probkowanie_layer.addFeature(feature)
                punkty += 1
            else:
                pass
    probkowanie_layer.updateExtents()
    probkowanie_layer.commitChanges()
    
    if feedback.isCanceled():
        return {}
    
    QgsVectorFileWriter.writeAsVectorFormatV3(
        layer = probkowanie_layer,
        fileName = sciezka_zapisu,
        transformContext = context.transformContext(),
        options = QgsVectorFileWriter.SaveVectorOptions()
    )
    
    return {"OUTPUT": sciezka_zapisu}