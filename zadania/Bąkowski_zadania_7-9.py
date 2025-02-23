import os

# Ustawienie ścieżki do pliku `powiaty.gpkg`
path = os.path.join(os.path.expanduser("~"), "Documents")
os.chdir(path)
filename = "powiaty.gpkg"
wektor = QgsVectorLayer(filename, "powiaty", "ogr")

def calculate_statistics(layer, field_name):
    """
    Oblicza podstawowe statystyki opisowe dla wskazanego pola warstwy.
    """
    values = [feature[field_name] for feature in layer.getFeatures() if feature[field_name] is not None]
    
    if not values:
        print(f"Pole {field_name} nie zawiera danych.")
        return None
    
    stats = {
        "min": min(values),
        "max": max(values),
        "mean": sum(values) / len(values),
        "count": len(values),
        "sum": sum(values)
    }
    print(f"Statystyki dla pola {field_name}: {stats}")
    return stats

# Obliczanie statystyk dla pól `powierzchnia` i `dlugosc`
if wektor.isValid():
    calculate_statistics(wektor, 'powierzchnia')  # Zmień nazwę pola na właściwą
    calculate_statistics(wektor, 'dlugosc')      # Zmień nazwę pola na właściwą
else:
    print("Warstwa nie została poprawnie załadowana.")
    
#-----------------------------------------------------------------------------------------------------#
import os

# Ustawienie ścieżki do pliku `powiaty.gpkg`
path = os.path.join(os.path.expanduser("~"), "Documents")
os.chdir(path)
filename = "powiaty.gpkg"
wektor = QgsVectorLayer(filename, "powiaty", "ogr")

def create_centroids_layer(input_layer, output_path):
    """
    Tworzy nową warstwę z centroidami dla powiatów i zapisuje ją na dysku w formacie .gpkg.
    """
    # Sprawdź, czy wejściowa warstwa jest poprawna
    if not input_layer or input_layer.geometryType() != QgsWkbTypes.PolygonGeometry:
        print("Warstwa wejściowa nie jest warstwą poligonową.")
        return False
    
    # Stwórz warstwę pamięciową dla centroidów
    centroids_layer = QgsVectorLayer("Point?crs=" + input_layer.crs().toWkt(), "Centroidy", "memory")
    centroids_provider = centroids_layer.dataProvider()
    
    # Skopiuj atrybuty z warstwy wejściowej
    centroids_provider.addAttributes(input_layer.fields())
    centroids_layer.updateFields()
    
    # Dodaj centroidy do nowej warstwy
    features = []
    for feature in input_layer.getFeatures():
        geom = feature.geometry()
        if geom:
            centroid = geom.centroid()
            new_feature = QgsFeature()
            new_feature.setGeometry(centroid)
            new_feature.setAttributes(feature.attributes())
            features.append(new_feature)
    
    centroids_provider.addFeatures(features)
    centroids_layer.updateExtents()
    
    # Zapisz warstwę na dysk
    error = QgsVectorFileWriter.writeAsVectorFormat(
        centroids_layer, 
        output_path, 
        "UTF-8", 
        input_layer.crs(), 
        "GPKG"
    )
    
    if error == QgsVectorFileWriter.NoError:
        print(f"Warstwa centroidów została zapisana w: {output_path}")
        return True
    else:
        print(f"Wystąpił błąd podczas zapisywania: {error}")
        return False

# Zapisanie centroidów do pliku .gpkg
output_path = os.path.join(path, "centroidy.gpkg")
if wektor.isValid():
    create_centroids_layer(wektor, output_path)
else:
    print("Warstwa nie została poprawnie załadowana.")