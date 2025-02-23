import math
import matplotlib.pyplot as plt
from qgis.core import QgsGeometry, QgsPointXY

# Część 1: Transformacja kolumn i wierszy na współrzędne geograficzne oraz odwrotnie
def xy_from_colrow(column, row, x_min, y_max, x_res, y_res):
    """
    Transformuje numer kolumny i wiersza na współrzędne geograficzne (x, y).
    """
    x = x_min + (column + 0.5) * x_res
    y = y_max - (row + 0.5) * y_res
    return x, y

def colrow_from_xy(x, y, x_min, y_max, x_res, y_res, cols, rows):
    """
    Transformuje współrzędne geograficzne (x, y) na numer kolumny i wiersza.
    Uwzględnia warunek sprawdzający czy punkty znajdują się w zakresie rastra.
    """
    column = math.floor((x - x_min) / x_res)
    row = math.floor((y_max - y) / y_res)
    if 0 <= column < cols and 0 <= row < rows:
        return column, row
    else:
        raise ValueError("Współrzędne poza zakresem rastra!")

# Część 2: Transformacje geometrii
def scale_geometry(wkt, scale_x, scale_y, pivot_x=0, pivot_y=0):
    """
    Skaluje geometrię względem podanego punktu obrotu.
    """
    geometry = QgsGeometry.fromWkt(wkt)
    geom_type = geometry.type().name
    vertices = geometry.vertices()
    scaled = []
    for vertex in vertices:
        new_x = scale_x * (vertex.x() - pivot_x) + pivot_x
        new_y = scale_y * (vertex.y() - pivot_y) + pivot_y
        scaled.append(QgsPointXY(new_x, new_y))
    if geom_type == "Point":
        return scaled
    elif geom_type == "Line":
        new_geom = QgsGeometry.fromPolylineXY(scaled)
    elif geom_type == "Polygon":
        new_geom = QgsGeometry.fromPolygonXY([scaled])
    else:
        raise ValueError("Nieobsługiwana geometria!")
    return new_geom

def rotate_geometry(wkt, angle, pivot_x=0, pivot_y=0):
    """
    Obraca geometrię o zadany kąt (w stopniach) wokół podanego punktu obrotu.
    """
    angle_rad = -angle * math.pi / 180  # Konwersja kąta na radiany
    geometry = QgsGeometry.fromWkt(wkt)
    geom_type = geometry.type().name
    vertices = geometry.vertices()
    rotated = []
    for vertex in vertices:
        new_x = ((vertex.x() - pivot_x) * math.cos(angle_rad) -
                 (vertex.y() - pivot_y) * math.sin(angle_rad) + pivot_x)
        new_y = ((vertex.x() - pivot_x) * math.sin(angle_rad) +
                 (vertex.y() - pivot_y) * math.cos(angle_rad) + pivot_y)
        rotated.append(QgsPointXY(new_x, new_y))
    if geom_type == "Point":
        return rotated
    elif geom_type == "Line":
        new_geom = QgsGeometry.fromPolylineXY(rotated)
    elif geom_type == "Polygon":
        new_geom = QgsGeometry.fromPolygonXY([rotated])
    else:
        raise ValueError("Nieobsługiwana geometria!")
    return new_geom

def geometry_to_coords(geometry):
    """
    Konwertuje obiekt QgsGeometry (lub WKT) do współrzędnych jako listy liczb.
    """
    if isinstance(geometry, str):
        geometry = QgsGeometry.fromWkt(geometry)
    geom_type = geometry.type().name
    if geom_type == "Point":
        x, y = geometry.asPoint()
    elif geom_type == "Line":
        points = geometry.asPolyline()
        x, y = zip(*[(p.x(), p.y()) for p in points])
    elif geom_type == "Polygon":
        points = geometry.asPolygon()
        x, y = zip(*[(p.x(), p.y()) for p in points[0]])
    else:
        raise ValueError("Nieobsługiwana geometria!")
    return x, y

# Przykładowy poligon
poly = "POLYGON ((40 30, 60 30, 50 40, 40 30))"

# Skalowanie
poly_scaled = scale_geometry(poly, scale_x=2, scale_y=1.5)

# Obrót
poly_rotated = rotate_geometry(poly, angle=45)

# Wizualizacja
x1, y1 = geometry_to_coords(poly)
x2, y2 = geometry_to_coords(poly_scaled)
x3, y3 = geometry_to_coords(poly_rotated)

plt.figure(figsize=(8, 6))
plt.plot(x1, y1, color="grey", linestyle="dashed", label="Oryginalny")
plt.fill(x2, y2, color="blue", alpha=0.5, label="Skalowany")
plt.fill(x3, y3, color="green", alpha=0.5, label="Obrócony")
plt.legend()
plt.title("Transformacje geometrii")
plt.show()
