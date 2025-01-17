from qgis.core import QgsPointXY, QgsCoordinateReferenceSystem

pt1 = (21.0122, 52.2296)
pt2 = (12.5113, 41.8919)

pt1 = QgsPointXY(pt1[0], pt1[1])
pt2 = QgsPointXY(pt2[0], pt2[1])

def haversine_distance(pt1, pt2):
    from math import sin, cos, asin, sqrt, pi
    r = 6371009 
    coords = [pt1.x(), pt1.y(), pt2.x(), pt2.y()]
    coords = [coord * pi / 180 for coord in coords]
    x1, y1, x2, y2 = coords
    delta_x = cos(x2 - x1)
    delta_y = cos(y2 - y1)
    d_t = 1 - delta_x + cos(x1)*cos(x2)*(1-delta_y)
    distance = 2 * r * asin(sqrt(d_t/2))
    distance = round(distance / 1000, 2)
    return distance
    
haversine_distance(pt1,pt2)