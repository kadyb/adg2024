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
    
    
def wyswietl_metadane(warstwa):
    if isinstance(warstwa, QgsVectorLayer):
        # Metadane dla warstwy wektorowej
        print("Typ warstwy: Wektorowa")
        print(f"Nazwa: {warstwa.name()}")
        print(f"Źródło danych: {warstwa.dataProvider().dataSourceUri()}")
        print(f"Liczba obiektów: {warstwa.featureCount()}")
        print(f"Typ geometrii: {warstwa.geometryType()}")
        print(f"CRS (układ odniesienia): {warstwa.crs().authid()}")
    elif isinstance(warstwa, QgsRasterLayer):
        # Metadane dla warstwy rastrowej
        print("Typ warstwy: Rastrowa")
        print(f"Nazwa: {warstwa.name()}")
        print(f"Źródło danych: {warstwa.source()}")
        print(f"Rozdzielczość: {warstwa.width()} x {warstwa.height()} (kolumny x wiersze)")
        print(f"Zakres przestrzenny: {warstwa.extent().toString()}")
        print(f"CRS (układ odniesienia): {warstwa.crs().authid()}")
    else:
        print("Nie rozpoznano typu warstwy. Upewnij się, że jest to warstwa wektorowa lub rastrowa.")

# Przykładowe użycie
sciezka_wektor = "powiaty.gpkg"
sciezka_raster = "DEM.tif"

wektor = QgsVectorLayer(sciezka_wektor, "Warstwa wektorowa", "ogr")
raster = QgsRasterLayer(sciezka_raster, "Warstwa rastrowa")

print("Metadane warstwy wektorowej:")
wyswietl_metadane(wektor)

print("\nMetadane warstwy rastrowej:")
wyswietl_metadane(raster)