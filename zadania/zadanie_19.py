from qgis.processing import alg
from qgis.core import (
    QgsVectorLayer, QgsFeature, QgsGeometry, QgsPointXY, QgsProject,
    QgsFields, QgsField
)
from qgis.PyQt.QtCore import QVariant
import random

@alg(name="losowe_punkty", label="Wylicz losowe punkty z poligonu - Marcel Tomczak 3 GI",
     group="examplescripts", group_label="Example scripts")
@alg.input(type=alg.VECTOR_LAYER, name="INPUT", label="Wprowadź pole wektorowe")
@alg.input(type=alg.INT, name="LICZBA_PUNKTOW", label="Liczba punktów", default=5)
@alg.output(type=alg.VECTOR_LAYER, name="", label="Warstwa wynikowa")

def losowe_punkty(instance, parameters, context, feedback, inputs):
    """
    Generuje losowe punkty wewnątrz poligonu i tworzy tymczasową warstwę w QGIS.
    """
    vector = instance.parameterAsVectorLayer(parameters, "INPUT", context)
    liczba_punktow = instance.parameterAsInt(parameters, "LICZBA_PUNKTOW", context)

    fields = QgsFields()
    fields.append(QgsField("id", QVariant.Int))

    crs = vector.crs().authid()
    output_layer = QgsVectorLayer("Point?crs=" + crs, "Losowe Punkty", "memory")
    provider = output_layer.dataProvider()
    
    provider.addAttributes(fields)
    output_layer.updateFields()

    features = []
    feature_id = 1

    if feedback.isCanceled():
        return {}

    for feature in vector.getFeatures():
        geom = feature.geometry()
        bbox = geom.boundingBox()
        for _ in range(liczba_punktow):
            while True:
                x = random.uniform(bbox.xMinimum(), bbox.xMaximum())
                y = random.uniform(bbox.yMinimum(), bbox.yMaximum())
                point = QgsPointXY(x, y)
                if geom.contains(QgsGeometry.fromPointXY(point)):
                    new_feature = QgsFeature()
                    new_feature.setGeometry(QgsGeometry.fromPointXY(point))
                    new_feature.setAttributes([feature_id])
                    features.append(new_feature)
                    feature_id += 1
                    break  

    provider.addFeatures(features)
    output_layer.updateExtents()

    QgsProject.instance().addMapLayer(output_layer)

    return {"OUTPUT_LAYER": output_layer}
