path = os.path.join(os.path.expanduser("~"),"Documents")
print(path)
os.chdir(path)

from qgis.core import QgsVectorLayer, QgsRasterLayer

def oblicz_wielkosc_komorki(sciezka_do_pliku):
    # Wczytaj raster
    raster = QgsRasterLayer(sciezka_do_pliku)
    
    if not raster.isValid():
        raise ValueError("Raster nie jest prawidłowy lub plik nie istnieje.")
    
    # Pobierz zakres przestrzenny (bounding box)
    extent = raster.extent()
    
    # Pobierz liczbę kolumn i wierszy rastra
    liczba_kolumn = raster.width()  # liczba kolumn
    liczba_wierszy = raster.height()  # liczba wierszy
    
    # Oblicz wielkość komórki
    wielkosc_komorki_x = extent.width() / liczba_kolumn
    wielkosc_komorki_y = extent.height() / liczba_wierszy
    
    return wielkosc_komorki_x, wielkosc_komorki_y

# Przykładowe użycie
sciezka_do_pliku = "DEM.tif"
try:
    wielkosc_komorki = oblicz_wielkosc_komorki(sciezka_do_pliku)
    print(f"Wielkość komórki (X, Y): {wielkosc_komorki}")
except ValueError as e:
    print(e)
    
 