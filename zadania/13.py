import random
from qgis.core import QgsVectorLayer, QgsFeature, QgsGeometry, QgsPointXY, QgsField, QgsProject, QgsVectorFileWriter
from qgis.PyQt.QtCore import QVariant

os.chdir("C:\\Users\\mixer\\Downloads\\adg")
filepath = os.path.join("powiaty.gpkg")
powiaty = QgsVectorLayer(filepath,"powiaty","ogr")

def generuj_losowe_punkty(warstwa, liczba_punktow, sciezka_zapisu=None):
    # Tworzenie nowej warstwy punktowej
    typ_geometrii = "Point"
    uklad_wspolrzednych = warstwa.crs().authid()
    nowa_warstwa = QgsVectorLayer(f"{typ_geometrii}?crs={uklad_wspolrzednych}", "Losowe_Punkty", "memory")
    
    # Dodanie atrybutu "id" do nowej warstwy
    dostawca = nowa_warstwa.dataProvider()
    dostawca.addAttributes([QgsField("id", QVariant.Int)])
    nowa_warstwa.updateFields()
    
    # Generowanie losowych punktów
    features = []
    for obiekt in warstwa.getFeatures():
        geometria = obiekt.geometry()
        granice = geometria.boundingBox()
        licznik = 0
        
        while licznik < liczba_punktow:
            wsp_x = random.uniform(granice.xMinimum(), granice.xMaximum())
            wsp_y = random.uniform(granice.yMinimum(), granice.yMaximum())
            punkt = QgsPointXY(wsp_x, wsp_y)
            
            if geometria.contains(QgsGeometry.fromPointXY(punkt)):
                nowy_obiekt = QgsFeature()
                nowy_obiekt.setGeometry(QgsGeometry.fromPointXY(punkt))
                nowy_obiekt.setAttributes([licznik])  # Ustawienie atrybutu "id"
                features.append(nowy_obiekt)
                licznik += 1
    
    # Dodanie wszystkich punktów do warstwy
    dostawca.addFeatures(features)
    nowa_warstwa.updateExtents()
    
    # Zapisanie warstwy do pliku (jeśli podano ścieżkę)
    if sciezka_zapisu:
        QgsVectorFileWriter.writeAsVectorFormat(nowa_warstwa, sciezka_zapisu, "UTF-8", nowa_warstwa.crs(), "GPKG")
    
    # Dodanie warstwy do projektu QGIS
    QgsProject.instance().addMapLayer(nowa_warstwa)
    
    return nowa_warstwa

# Przykład użycia
generuj_losowe_punkty(powiaty, 50, "D:/sezon3/lowowe_pkt.gpkg")