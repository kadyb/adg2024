from qgis.processing import alg
from qgis.core import QgsVectorLayer, QgsFeature, QgsVectorFileWriter
import statistics as stats_module
import os

@alg(name="layerstats", label="Calculate layer statistics",
     group="examplescripts", group_label="Example scripts")
@alg.input(type=alg.SOURCE, name="INPUT", label="Input vector layer")
@alg.output(type=alg.BOOL, name="OUTPUT", label="Statistics calculated")
def layerstats(instance, parameters, context, feedback, inputs):
    """
    Calculates basic descriptive statistics for area and border length.
    """
    
    layer = instance.parameterAsVectorLayer(parameters, "INPUT", context)
   
    if feedback.isCanceled():
        return {}
    
    border_lengths = []
    area_values = []
    for feature_item in layer.getFeatures():
        border_lengths.append(feature_item.attribute("dl_granicy"))
        area_values.append(feature_item.geometry().area() / 1000**2)

    feedback.pushInfo("Statystyki dla długości granic:\nśrednia: {}\nmediana: {}\nminimum: {}\nmaksimum: {}\nodchylenie standardowe: {}".format(
        stats_module.mean(border_lengths), 
        stats_module.median(border_lengths), 
        min(border_lengths), 
        max(border_lengths), 
        stats_module.stdev(border_lengths)
    ))
    feedback.pushInfo("Statystyki dla powierzchni:\nśrednia: {}\nmediana: {}\nminimum: {}\nmaksimum: {}\nodchylenie standardowe: {}".format(
        stats_module.mean(area_values),
        stats_module.median(area_values),
        min(area_values),
        max(area_values),
        stats_module.stdev(area_values)
    ))

    return {"OUTPUT": True}