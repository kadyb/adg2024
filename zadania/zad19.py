import qgis.core as qc
from qgis.processing import alg
import random

@alg(name = "points", label = "Random stratifed points",
     group = "examplescripts" , group_label = "Example scripts")
@alg.input(type = alg.SOURCE, name = "INPUT", label = "Input point vector layer")
@alg.input(type = alg.INT, name = "NUMPOINT", label = "Number of points per feature", default = 1)
@alg.input(type = alg.VECTOR_LAYER_DEST, name = "OUTPUT_PATH", label = "Stratified points")
@alg.output(type = alg.FILE, name = "OUTPUT", label = "Stratified points")

def random_points(instance, parameters, context, feedback, inputs):
    """
    Create random points with stratification, simplified version
    """
    
    layer = instance.parameterAsVectorLayer(parameters, "INPUT", context)
    num_point = instance.parameterAsInt(parameters, "NUMPOINT", context)
    output_path = instance.parameterAsOutputLayer(parameters, "OUTPUT_PATH", context)
    
    crs = layer.crs().authid()
    vect = qc.QgsVectorLayer("Point?crs=" + crs, "Random points (stratified)", "memory")
    

    
    for feature in layer.getFeatures():
        if feedback.isCanceled():
            break
        
        bbox = feature.geometry().boundingBox()
        t = 0
        while t < num_point:
            new_feat = qc.QgsFeature()
            x = bbox.xMinimum() + bbox.width() * random.random()
            y = bbox.yMinimum() + bbox.height() * random.random()
            pt = qc.QgsGeometry().fromPointXY(qc.QgsPointXY(x,y))
            if pt.within(feature.geometry()) is True:
                new_feat.setGeometry(pt)
                vect.dataProvider().addFeature(new_feat)
                t += 1
    vect.updateExtents()
    
    
    if feedback.isCanceled():
        return {}
    
    qc.QgsVectorFileWriter.writeAsVectorFormatV3(
        layer = vect,
        fileName = output_path,
        transformContext = context.transformContext(),
        options = qc.QgsVectorFileWriter.SaveVectorOptions()
    )
    
    return {"OUTPUT": output_path}
