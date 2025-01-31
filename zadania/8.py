import statistics
import numpy as np

os.chdir("C:\\Users\\mixer\\Downloads\\adg")
filepath = os.path.join("powiaty.gpkg")
vector = QgsVectorLayer(filepath,"powiaty","ogr")

print(vector.isValid())
QgsProject.instance().addMapLayer(vector)

#############

def statystyki_opisowe(vector):
    powierzchnia=[]
    dlugosc=[]
    
    for feature in vector.getFeatures():
        geometry = feature.geometry()
        powierzchnia.append(geometry.area())
        dlugosc.append(geometry.length())
        
    powierzchnia_stats = {
        'minimum' : np.min(powierzchnia),
        'srednia' : statistics.mean(powierzchnia),
        'mediana' : statistics.median(powierzchnia),
        'max' : np.max(powierzchnia),
        'odchylenie standardowe' : statistics.stdev(powierzchnia),
        'suma' : np.sum(powierzchnia)
        }
        
    dlugosc_stats = {
        'minimum' : np.min(dlugosc),
        'srednia' : statistics.mean(dlugosc),
        'mediana' : statistics.median(dlugosc),
        'max' : np.max(dlugosc),
        'odchylenie standardowe' : statistics.stdev(dlugosc),
        'suma' : np.sum(dlugosc)
        }
        
    print(f"Statystyki dla powierzchni:\n{powierzchnia_stats}")
    print(f"\nStatystyki dla długości:\n{dlugosc_stats}")

statystyki_opisowe(vector)




###########################






