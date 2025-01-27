import statistics as stat
import qgis.core

path = os.path.join(os.path.expanduser("~"), "Documents", "dane")
os.chdir(path)

file = "powiaty.gpkg"
vector = QgsVectorLayer(file)

def powiaty_stats(vector):
    ls = []
    areas = []
    for f in vector.getFeatures():
        ls.append(f.attribute("dl_granicy"))
    for f in vector.getFeatures():
        areas.append(f.attribute("pole_km2"))
    print("Statistics for border length:\nmean: {}\nmedian: {}\nmin: {}\nmax: {}\nstandard deviation: {}".format(stat.mean(ls), stat.median(ls), min(ls), max(ls), stat.stdev(ls)))
    print("Statistics for area:\nmean: {}\nmedian: {}\nmin: {}\nmax: {}\nstandard deviation: {}".format(stat.mean(areas), stat.median(areas), min(areas), max(areas), stat.stdev(areas)))

powiaty_stats(vector)