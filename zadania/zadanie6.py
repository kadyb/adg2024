from qgis.core import QgsVectorLayer, QgsRasterLayer

path = os.path.join(os.path.expanduser("~"),"Documents", "algorytmy", "dane")
os.chdir(path)

def metadane(warstwa):
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
        print("Nieprawidłowy typ warstwy ")

# Przykładowe użycie
sciezka_wektor = "powiaty.gpkg"
sciezka_raster = "DEM.tif"

wektor = QgsVectorLayer(sciezka_wektor, "Warstwa wektorowa", "ogr")
raster = QgsRasterLayer(sciezka_raster, "Warstwa rastrowa")

metadane(wektor)
metadane(raster)