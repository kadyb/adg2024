import os
import qgis.core as qg
import matplotlib.pyplot as plt

path = os.path.join(os.path.expanduser("~"),"Documents/adg/06")
os.chdir(path)

# zad 18 Zaimplementuj dwie wybrane operacje transformacji geometrii, a następnie wyświetl ich 
# wyniki. Jako przykładowe dane wykorzystaj poligon "POLYGON ((40 30, 60 30, 50 40, 40 30))".

poligon = "POLYGON ((40 30, 60 30, 50 40, 40 30))"

# przesuniecie
geometry = QgsGeometry.fromWkt(poligon)
geom_type = geometry.type().name
vertices = geometry.vertices()
    
shifted = []
for vertex in vertices:
    new_x = vertex.x() + 10
    new_y = vertex.y() + 5
    shifted.append(QgsPointXY(new_x, new_y))

new_geom = QgsGeometry.fromPolygonXY([shifted])

# wizualizacja
def geometry_to_coords(geometry):
    from qgis.core import QgsGeometry
    
    if isinstance(geometry, str):
        geometry = QgsGeometry.fromWkt(geometry)
    
    geom_type = geometry.type().name
    
    points = geometry.asPolygon()
    for p in points:
        x, y = zip(*p)
    return x, y
    
x1 = geometry_to_coords(poligon)[0]
y1 = geometry_to_coords(poligon)[1]
x2 = geometry_to_coords(new_geom)[0]
y2 = geometry_to_coords(new_geom)[1]

plt.figure(figsize = (4, 3))
plt.plot(x1, y1, color = "grey", linestyle = "dashed", zorder = 1)
plt.fill(x2, y2, color = "blue", zorder = 2)
plt.title("Przesunięcie (dx = 10, dy = 5)")
plt.show()

# obrócenie
a = 5

odbicie = []
for vertex in vertices:
    new_x = 2 * a - vertex.x()
    new_y = vertex.y()
    odbicie.append(QgsPointXY(new_x, new_y))

new_geom2 = QgsGeometry.fromPolygonXY([odbicie])

# wizualizacja
x1 = geometry_to_coords(poligon)[0]
y1 = geometry_to_coords(poligon)[1]
x2 = geometry_to_coords(new_geom2)[0]
y2 = geometry_to_coords(new_geom2)[1]

plt.figure(figsize = (4, 3))
plt.plot(x1, y1, color = "grey", linestyle = "dashed", zorder = 1)
plt.fill(x2, y2, color = "blue", zorder = 2)
plt.title("Odbicie (a = 5)")
plt.show()


