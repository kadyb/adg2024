from qgis.core import (
    QgsVectorLayer,
    QgsFeature,
    QgsVectorFileWriter,
    QgsProject
)

# 🔹 Ścieżka do pliku wejściowego (powiaty)
input_path = "C:/Users/user/Desktop/ADG/Zajecia_1/Dane/powiaty.gpkg"

# 🔹 Ścieżka do pliku wyjściowego (centroidy)
output_path = "C:/Users/user/Desktop/ADG/Zajecia_1/Dane/centroidy.gpkg"

# Wczytanie warstwy wektorowej powiatów
layer = QgsVectorLayer(input_path, "Powiaty", "ogr")

# Sprawdzenie, czy warstwa została poprawnie wczytana
if not layer.isValid():
    print("Błąd: Nie można wczytać warstwy!")
else:
    print(f"Wczytano warstwę: {layer.name()}")
    # Tworzenie nowej warstwy dla centroidów
    crs = layer.crs().authid()
    centroid_layer = QgsVectorLayer(f"Point?crs={crs}", "Centroids", "memory")
    # Tworzenie obiektów centroidów
    features = []
    for feature in layer.getFeatures():
        geom = feature.geometry()
        centroid_geom = geom.centroid()
        centroid_feature = QgsFeature()
        centroid_feature.setGeometry(centroid_geom)
        features.append(centroid_feature)
    # Dodanie obiektów do warstwy centroidów
    centroid_layer.dataProvider().addFeatures(features)
    centroid_layer.updateExtents()
    # Zapisanie wyników do pliku GeoPackage
    QgsVectorFileWriter.writeAsVectorFormatV3(
        layer=centroid_layer,
        fileName=output_path,
        transformContext=QgsProject.instance().transformContext(),
        options=QgsVectorFileWriter.SaveVectorOptions()
    )
    print(f"Zapisano centroidy do pliku: {output_path}")