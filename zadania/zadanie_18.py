import os 
import qgis.core
import math
import matplotlib.pyplot as plt

wkt = "POLYGON ((40 30, 60 30, 50 40, 40 30))"

def geom_transpose(wkt):
    geom = QgsGeometry.fromWkt(wkt)
    geom_type = geom.type().name
    vertices = geom.vertices()
    
    transposed = []
    for vertex in vertices:
        new_x = vertex.y()
        new_y = vertex.x()
        transposed.append(QgsPointXY(new_x, new_y))
    
    if geom_type == "Point":
        return transposed
    elif geom_type == "Line":
        geom_transposed = QgsGeometry.fromPolylineXY(transposed)
    elif geom_type == "Polygon":
        geom_transposed = QgsGeometry.fromPolygonXY([transposed])
        
    return geom_transposed

def geom_rotate(wkt, angle):
    if type(angle) is int or type(angle) is float:
        geom = QgsGeometry.fromWkt(wkt)
        geom_type = geom.type().name
        vertices = geom.vertices()
        centroid = geom.centroid().asPoint()
        
        rad = (angle * math.pi) / 180
        rotated = []
        for vertex in vertices:
            new_x = (vertex.x() - centroid.x()) * math.cos(rad) - (vertex.y() - centroid.y()) * math.sin(rad) + centroid.x()
            new_y = (vertex.x() - centroid.x()) * math.sin(rad) + (vertex.y() - centroid.y()) * math.cos(rad) + centroid.y()
            rotated.append(QgsPointXY(new_x, new_y))
    
    if geom_type == "Line":
        geom_rotated = QgsGeometry.fromPolylineXY(rotated)
    elif geom_type == "Polygon":
        geom_rotated = QgsGeometry.fromPolygonXY([rotated])
    
    return geom_rotated

def geometry_to_coords(geometry):    
    if isinstance(geometry, str):
        geometry = QgsGeometry.fromWkt(geometry)
    geom_type = geometry.type().name
    if geom_type == "Point":
        x, y = geometry.asPoint()
    elif geom_type == "Line":
        points = geometry.asPolyline()
        x, y = zip(*points)
    elif geom_type == "Polygon":
        points = geometry.asPolygon()
        for p in points:
            x, y = zip(*p)
    else:
        raise ValueError("Nieobsługiwana geometria!")
    
    return x, y

transposed = geom_transpose(wkt)
rotated = geom_rotate(wkt, 180)

x1 = geometry_to_coords(wkt)[0]
y1 = geometry_to_coords(wkt)[1]
x2 = geometry_to_coords(transposed)[0]
y2 = geometry_to_coords(transposed)[1]
x3 = geometry_to_coords(rotated)[0]
y3 = geometry_to_coords(rotated)[1]

plt.figure(figsize = (4, 3))
plt.plot(x1, y1, color = "grey", linestyle = "dashed", zorder = 1, label = "oryginał")
plt.fill(x2, y2, color = "blue", zorder = 2, label = "transpozycja")
plt.fill(x3, y3, color = "green", zorder = 2, label = "obrót")
plt.title("Transformacje geometrii")
plt.legend()
plt.show()