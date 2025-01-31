import random
from qgis.core import QgsVectorLayer, QgsFeature, QgsGeometry, QgsPointXY, QgsField, QgsProject, QgsVectorFileWriter
from qgis.PyQt.QtCore import QVariant

os.chdir("C:\\Users\\mixer\\Downloads\\adg")
filepath = os.path.join("powiaty.gpkg")
powiaty = QgsVectorLayer(filepath,"powiaty","ogr")

def generuj_losowe_punkty(warstwa, liczba_punktow, sciezka_zapisu=None):
    typ_geometrii = "Point"
    uklad_wspolrzednych = warstwa.crs().authid()
    nowa_warstwa = QgsVectorLayer(f"{typ_geometrii}?crs={uklad_wspolrzednych}", "Losowe_Punkty", "memory")
    
    dostawca = nowa_warstwa.dataProvider()
    dostawca.addAttributes([QgsField("id", QVariant.Int)])
    nowa_warstwa.updateFields()
    
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
    
    dostawca.addFeatures(features)
    nowa_warstwa.updateExtents()
    
    if sciezka_zapisu:
        QgsVectorFileWriter.writeAsVectorFormat(nowa_warstwa, sciezka_zapisu, "UTF-8", nowa_warstwa.crs(), "GPKG")
    
    QgsProject.instance().addMapLayer(nowa_warstwa)
    
    return nowa_warstwa

generuj_losowe_punkty(powiaty, 50, "D:/sezon3/lowowe_pkt.gpkg")