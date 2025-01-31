#Zaimplementuj dwie wybrane operacje transformacji geometrii, a następnie wyświetl ich wyniki. 
#Jako przykładowe dane wykorzystaj poligon "POLYGON ((40 30, 60 30, 50 40, 40 30))".
#Marcel Tomczak 3 GI
import matplotlib.pyplot as plt

def odbicie_trans(wkt, a, b, c):
    
    
    geometry = QgsGeometry.fromWkt(wkt)
    geom_type = QgsWkbTypes.displayString(geometry.wkbType())
    vertices = list(geometry.vertices())
    
    odbicie_trans = []
    for vertex in vertices:
        new_x = vertex.x()
        new_y = vertex.y()
        if a is not None:
            new_x = 2 * a - vertex.x()
        if b is not None:
            new_y = 2 * b - vertex.y()
        
        if c:
            new_x, new_y = new_y, new_x
        
        odbicie_trans.append(QgsPointXY(new_x, new_y))
    
    if geom_type == "Point":
        return odbicie_trans
    elif geom_type == "LineString":
        new_geom = QgsGeometry.fromPolylineXY(odbicie_trans)
    elif geom_type == "Polygon":
        new_geom = QgsGeometry.fromPolygonXY([odbicie_trans])
    else:
        raise ValueError("Nieobsługiwana geometria!")
    
    return new_geom


def geometry_to_coords(geometry):
    from qgis.core import QgsGeometry
    
    if isinstance(geometry, str):
        geometry = QgsGeometry.fromWkt(geometry)
    
    geom_type = QgsWkbTypes.displayString(geometry.wkbType())
    
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

poly = "POLYGON ((40 30, 60 30, 50 40, 40 30))"
poly_odbicie_trans = odbicie_trans(poly, a = 10, b = 5, c = True)
print(poly_odbicie_trans)


x1 = geometry_to_coords(poly)[0]
y1 = geometry_to_coords(poly)[1]
x2 = geometry_to_coords(poly_odbicie_trans)[0]
y2 = geometry_to_coords(poly_odbicie_trans)[1]


plt.figure(figsize = (4, 3))
plt.plot(x1, y1, color = "grey", linestyle = "dashed", zorder = 1)
plt.fill(x2, y2, color = "blue", zorder = 2)
plt.title("Odbicie i transpozycja")
plt.show()

