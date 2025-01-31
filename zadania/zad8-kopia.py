'''
Napisz funkcję, która obliczy podstawowe statystyki opisowe i zastosuj ją
dla powierzchni oraz długości.
'''

import statistics as stats_module
from qgis.core import QgsVectorLayer
import os

data_directory = "/Users/michalbaczkiewicz/Documents/GitHub/adg2024/dane/"
os.chdir(data_directory)
file_name = "powiaty.gpkg"
layer_obj = QgsVectorLayer(file_name, "powiaty", "ogr")

def calculate_layer_stats(layer):
        border_lengths = []
        area_values = []
        for feature_item in layer.getFeatures():
            border_lengths.append(feature_item.attribute("dl_granicy"))
            area_values.append(feature_item.geometry().area() / 1000**2)
        print("Statystyki dla długości granic:\nśrednia: {}\nmediana: {}\nminimum: {}\nmaksimum: {}\nodchylenie standardowe: {}".format(
            stats_module.mean(border_lengths), 
            stats_module.median(border_lengths), 
            min(border_lengths), 
            max(border_lengths), 
            stats_module.stdev(border_lengths)
        ))
        print("Statystyki dla powierzchni:\nśrednia: {}\nmediana: {}\nminimum: {}\nmaksimum: {}\nodchylenie standardowe: {}".format(
            stats_module.mean(area_values),
            stats_module.median(area_values),
            min(area_values),
            max(area_values),
            stats_module.stdev(area_values)
        ))

calculate_layer_stats(layer_obj)


