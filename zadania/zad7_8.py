#%% zadanie 7

import os
import numpy as np
import qgis.core as qc
from statistics import mean, stdev
from qgis.PyQt.QtCore import QMetaType

path = os.path.join(os.path.expanduser('~'),'algorytmy_geo')
vect_path = os.path.join(path,'dane','powiaty.gpkg')
vect = qc.QgsVectorLayer(vect_path)

vect.startEditing()

new_field = [qc.QgsField("dlugosc_m", QMetaType.Type.Double)]
vect.dataProvider().addAttributes(new_field)
vect.updateFields()

area_idx = vect.fields().indexOf("dlugosc_m")

for feat in vect.getFeatures():
    length = 0
    for polygon in feat.geometry().asMultiPolygon():
        for line in polygon:
            line_len = qc.QgsGeometry(qc.QgsLineString(line))
            length += line_len.length()
               
    vect.changeAttributeValue(feat.id(), area_idx, length)
    
vect.commitChanges()

#%% zadanie 8

def DescStat(layer, attr):
    stats = [feat[attr] for feat in layer.getFeatures() if feat[attr] is not None]
    return {"liczba wartości": len(stats),
            "minimum": np.quantile(stats, 0),
            "pierwszy kwartyl": np.quantile(stats, 0.25),
            "średnia": mean(stats),
            "mediana": np.quantile(stats, 0.5),
            "trzeci kwartyl": np.quantile(stats, 0.75),
            "maksimum": np.quantile(stats, 1),
            "odchylenie standardowe": stdev(stats)}
    
DescStat(vect, 'dlugosc_m')
DescStat(vect, 'pole_km2')
