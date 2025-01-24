from shapely.geometry import Polygon
from shapely.affinity import scale, rotate
import matplotlib.pyplot as plt

# Funkcja do rysowania poligonów
def plot_polygon(polygon, title, color):
    x, y = polygon.exterior.xy
    plt.plot(x, y, label=title, color=color)
    plt.fill(x, y, alpha=0.3, color=color)

# Oryginalny poligon
original_polygon = Polygon([(40, 30), (60, 30), (50, 40), (40, 30)])

# Odbicie względem osi Y (zmiana znaku współrzędnej X)
mirrored_polygon = scale(original_polygon, xfact=-1, yfact=1, origin='centroid')

# Obrót o 45 stopni wokół centroidu
rotated_polygon = rotate(original_polygon, angle=45, origin='centroid')

# Tworzenie wykresu
plt.figure(figsize=(8, 6))
plot_polygon(original_polygon, 'Oryginalny', 'blue')
plot_polygon(mirrored_polygon, 'Odbicie (Y)', 'red')
plot_polygon(rotated_polygon, 'Obrót (45°)', 'green')

plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Transformacje Geometrii: Odbicie i Obrót')
plt.grid(True)
plt.show()
