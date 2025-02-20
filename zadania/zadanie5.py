from qgis.core import QgsVectorLayer, QgsRasterLayer

filepath = os.path.join(os.path.expanduser("~"),"Documents", "algorytmy", "dane")

print(filepath)
os.chdir(filepath)

def wielkosc_komorki(sciezka):
    # Wczytaj raster
    raster = QgsRasterLayer(sciezka)
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
sciezka = "DEM.tif"

wielkosc_kom = wielkosc_komorki(sciezka)
print(f"Wielkość komórki (X, Y): {wielkosc_kom}")