import matplotlib.pyplot as plt

poly = "POLYGON ((40 30, 60 30, 50 40, 40 30))"

def transposition(wkt):
    from qgis.core import QgsGeometry, QgsPointXY
    
    geometry = QgsGeometry.fromWkt(wkt)
    geom_type = geometry.type().name
    vertices = geometry.vertices()
    
    transpositioned = []
    for vertex in vertices:
        new_x = vertex.y()
        new_y = vertex.x()
        transpositioned.append(QgsPointXY(new_x, new_y))
    
    if geom_type == "Point":
        return transpositioned
    elif geom_type == "Line":
        transpositioned = QgsGeometry.fromPolylineXY(transpositioned)
    elif geom_type == "Polygon":
        transpositioned = QgsGeometry.fromPolygonXY([transpositioned])
    else:
        raise ValueError("Nieobsługiwana geometria!")
    
    return transpositioned


transpositioned = transposition(poly)
print(transpositioned)



def scaling(wkt, scale):
    from qgis.core import QgsGeometry, QgsPointXY
    
    geometry = QgsGeometry.fromWkt(wkt)
    centroid = geometry.centroid()
    px = geometry.centroid().asPoint().x()
    py = geometry.centroid().asPoint().y()
    geom_type = geometry.type().name
    vertices = geometry.vertices()
    
    scaled = []
    for vertex in vertices:
        new_x = scale * (vertex.x() - px) + px
        new_y = scale * (vertex.y() - py) + py
        scaled.append(QgsPointXY(new_x, new_y))
    
    if geom_type == "Point":
        return scaled
    elif geom_type == "Line":
        scaled = QgsGeometry.fromPolylineXY(scaled)
    elif geom_type == "Polygon":
        scaled = QgsGeometry.fromPolygonXY([scaled])
    else:
        raise ValueError("Nieobsługiwana geometria!")
    
    return scaled

scaled = scaling(poly,2)
print(scaled)



def geometry_to_coords(geometry):
    from qgis.core import QgsGeometry
    
    # przypadek geometrii z WKT
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



x1 = geometry_to_coords(transpositioned)[0]
y1 = geometry_to_coords(transpositioned)[1]
x2 = geometry_to_coords(scaled)[0]
y2 = geometry_to_coords(scaled)[1]

plt.figure(figsize = (4, 3))
plt.plot(x1, y1, color = "blue", linestyle = "dashed", zorder = 1)
plt.fill(x2, y2, color = "grey", zorder = 2)
plt.show()





