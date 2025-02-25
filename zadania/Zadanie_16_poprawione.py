import csv
import math
import os

# Ustal ścieżkę do folderu Dokumenty
path = os.path.join(os.path.expanduser("~"), "Documents")
os.chdir(path)

csv_file = "profil.csv"

def surface_distance(pt1, pt2):
    x1, y1, z1 = pt1
    x2, y2, z2 = pt2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

def calculate_total_surface_distance(csv_file):
    total_distance = 0.0
    points = []
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Pominięcie nagłówka
        for row in reader:
            if len(row) < 4:  # ID + X + Y + Z
                print(f"Pominięto nieprawidłowy wiersz: {row}")
                continue
            try:
                x, y, z = map(float, row[1:4])  # Pobierz kolumny 2, 3, 4
                points.append((x, y, z))
            except ValueError as e:
                print(f"Błąd konwersji wiersza {row}: {e}")
    for i in range(len(points) - 1):
        total_distance += surface_distance(points[i], points[i + 1])
    return total_distance

# Przykład użycia
total_length = calculate_total_surface_distance(csv_file)
print(f"Całkowita długość profilu terenu: {total_length:.2f} m")


