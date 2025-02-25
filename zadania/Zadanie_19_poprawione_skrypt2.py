from qgis.processing import alg
import csv
import math
import os

@alg(name="terrain_profile_length", label="Calculate Terrain Profile Length",
     group="examplescripts", group_label="Example scripts")
@alg.input(type=alg.FILE, name="CSV_FILE", label="CSV file with profile data")
@alg.output(type=alg.STRING, name="OUTPUT", label="Total terrain profile length")

def terrain_profile_length(instance, parameters, context, feedback, inputs):
    """
    Oblicz całkowitą długość profilu terenu na podstawie współrzędnych 3D z pliku CSV.
    """
    csv_file = instance.parameterAsFile(parameters, "CSV_FILE", context)
    total_distance = 0.0
    points = []
    def surface_distance(pt1, pt2):
        x1, y1, z1 = pt1
        x2, y2, z2 = pt2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    # Wczytaj dane z pliku CSV
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Pominięcie nagłówka
        for row in reader:
            if len(row) < 4:  # Sprawdzenie, czy są ID, X, Y, Z
                feedback.reportError(f"Pominięto nieprawidłowy wiersz: {row}")
                continue
            try:
                x, y, z = map(float, row[1:4])  # Pobierz kolumny 2, 3, 4
                points.append((x, y, z))
            except ValueError as e:
                feedback.reportError(f"Błąd konwersji wiersza {row}: {e}")
    # Oblicz całkowitą odległość
    for i in range(len(points) - 1):
        total_distance += surface_distance(points[i], points[i + 1])
    return {"OUTPUT": f"Całkowita długość profilu terenu: {total_distance:.2f} m"}
