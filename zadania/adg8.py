#ad8
import numpy as np

def cal_stats(layer):
    areas = []
    lengths = []
    for feature in layer.getFeatures():
        geom = feature.geometry()
        areas.append(geom.area())
        lengths.append(geom.length())
    def stats(values):
        return{
        "min": np.min(values),
        "max": np.max(values),
        "mean": np.mean(values),
        "median": np.median(values),
        "std_dev": np.std(values)
        }
    return {"area": stats(areas), "length": stats(lengths)}

vector_layer = QgsVectorLayer("powiaty.gpkg", "powiaty", "ogr")
stats = cal_stats(vector_layer)
print("Statystyki dla powierzchni:", stats["area"])
print("Statystyki dla długości:", stats["length"])