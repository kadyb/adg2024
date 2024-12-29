import os
from qgis.core import QgsVectorLayer
from qgis.core import QgsRasterLayer

path = os.path.join(os.path.expanduser("~"),"Documents/adg/01")
os.chdir(path)

wektor = QgsVectorLayer("powiaty.gpkg")
raster = QgsRasterLayer("DEM.tif")

# 6 Napisz funkcję (wyswietl_metadane), która zaprezentuje metadane warstwy 
# wektorowej oraz rastrowej w czytelny sposób. Do sprawdzenia typu obiektu 
# wykorzystaj funkcję isinstance (QgsVectorLayer lub QgsRasterLayer)

def wyswietl_metadane(warstwa):
    if isinstance(warstwa, QgsVectorLayer):
        rodzaj_geometrii = warstwa.geometryType()
        rodzaj_geometrii = rodzaj_geometrii.name  # zwraca nazwę
        zakres = warstwa.extent()  # obiekt QgsRectangle
        zakres = zakres.toString()  # konwersja na tekst
        liczba_obiekty = warstwa.featureCount()
        liczba_atrybuty = warstwa.fields()
        liczba_atrybuty = liczba_atrybuty.count()
        uklad = warstwa.crs()
        uklad = uklad.authid()  # zwraca kod EPSG
        return (
            f"Rodzaj geometrii: {rodzaj_geometrii} "
            f"Zakres przestrzenny: {zakres} "
            f"Liczba obiektów: {liczba_obiekty} "
            f"Liczba atrybutów: {liczba_atrybuty} "
            f"Układ współrzędnych: {uklad} "
            )
    elif isinstance(warstwa, QgsRasterLayer):
        szerokosc = warstwa.width()
        wysokosc = warstwa.height()
        liczba_kanalow = warstwa.bandCount()
        zakres = warstwa.extent().toString()
        crs = warstwa.crs().authid()
        rozdzielczosc = (warstwa.rasterUnitsPerPixelX(), warstwa.rasterUnitsPerPixelY())
        return (
            f"Liczba kolumn: {szerokosc} "
            f"Liczba wierszy: {wysokosc} "
            f"Liczba kanałów: {liczba_kanalow} "
            f"Zakres: {zakres} "
            f"CRS: {crs} "
            f"Rozdzielczość: {rozdzielczosc}")

wyswietl_metadane(wektor)
wyswietl_metadane(raster)
