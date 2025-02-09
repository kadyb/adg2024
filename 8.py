import numpy as np

os.chdir("C:\\Users\\mixer\\Downloads\\adg")
filepath = os.path.join("powiaty.gpkg")
vector = QgsVectorLayer(filepath,"powiaty","ogr")

print(vector.isValid())
QgsProject.instance().addMapLayer(vector)

#############

def stats(vector):
    powierzchnia=[]
    dlugosc=[]  
    for feature in vector.getFeatures():
        geom = feature.geometry()
        powierzchnia.append(geom.area())
        dlugosc.append(geom.length())
    powierzchnia_stats = {
        'minimum' : np.min(powierzchnia),
        'srednia' : np.mean(powierzchnia),
        'mediana' : np.median(powierzchnia),
        'max' : np.max(powierzchnia),
        'suma' : np.sum(powierzchnia)
        }
    dlugosc_stats = {
        'minimum' : np.min(dlugosc),
        'srednia' : np.mean(dlugosc),
        'mediana' : np.median(dlugosc),
        'max' : np.max(dlugosc),,
        'suma' : np.sum(dlugosc)
        }
    print(f"Powierzchnia:{powierzchnia_stats}")
    print(f"Dlugosc:{dlugosc_stats}")

stats(vector)










