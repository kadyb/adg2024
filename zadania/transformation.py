from osgeo import gdal
from qgis.core import QgsGeometry
import matplotlib.pyplot as plt

def xy_from_colrow(raster, col, row):
    transform = raster.GetGeoTransform()
    
    if 0 <= col < raster.RasterXSize and 0 <= row < raster.RasterYSize:
        x = transform[0] + col * transform[1] + row * transform[2]
        y = transform[3] + col * transform[4] + row * transform[5]
        return x, y
    else:
        raise ValueError("Współrzędne poza zakresem rastra")

def colrow_from_xy(raster, x, y):
    transform = raster.GetGeoTransform()
    inv_transform = gdal.InvGeoTransform(transform)  # Odwrócona transformacja
    col, row = gdal.ApplyGeoTransform(inv_transform, x, y)

    col, row = int(round(col)), int(round(row))

    if 0 <= col < raster.RasterXSize and 0 <= row < raster.RasterYSize:
        return col, row
    else:
        raise ValueError("Współrzędne poza zakresem rastra")

def geometry_to_coords(geometry):
    
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
    
def rotate(geometry, angle, px, py):
    geom_type = geometry.type().name
    theta = -angle * np.pi / 180

    rotated = []
    for vertex in geometry.vertices():
        x = vertex.x()
        y = vertex.y()
        x_new = (x - px) * np.cos(theta) - (y - py) * np.sin(theta) + px
        y_new = (x - px) * np.sin(theta) + (y - py) * np.cos(theta) + py
        rotated.append(QgsPointXY(x_new, y_new))
        
    if geom_type == "Point":
        return shifted
    elif geom_type == "Line":
        new_geom = QgsGeometry.fromPolylineXY(rotated)
    elif geom_type == "Polygon":
        new_geom = QgsGeometry.fromPolygonXY([rotated])
    else:
        raise ValueError("Nieobsługiwana geometria!")
    
    return new_geom
    
def horizontalReflect(geometry, b):
    geom_type = geometry.type().name

    reflected = []
    for vertex in geometry.vertices():
        x_new = vertex.x()
        y_new = b*2 - vertex.y()
        reflected.append(QgsPointXY(x_new, y_new))
    
    if geom_type == "Point":
        return shifted
    elif geom_type == "Line":
        new_geom = QgsGeometry.fromPolylineXY(reflected)
    elif geom_type == "Polygon":
        new_geom = QgsGeometry.fromPolygonXY([reflected])
    else:
        raise ValueError("Nieobsługiwana geometria!")
        
    return new_geom

def main():
    rasterPath = "C:/Users/tymon/OneDrive/Pulpit/Projects/Justyna/Algorytmy/Dane/DEM.tif"
    raster = gdal.Open(rasterPath)
    rasterLayer = QgsRasterLayer(rasterPath, "DEM")
    
    print("Liczba kolumn (Szerokość):", rasterLayer.width())
    print("Liczba wierszy (Wysokość):", rasterLayer.height())
    print("Liczba komórek:", rasterLayer.height() * rasterLayer.height())
    print("Liczba kanałów:", rasterLayer.bandCount())
    print("Zakres:", rasterLayer.extent().toString(precision = 2))
    print("CRS:", rasterLayer.crs().authid())
    
    col, row = 10, 20
    x, y = xy_from_colrow(raster, col, row)
    print(f"Kolumna {col}, Wiersz {row} -> Współrzędne: ({x}, {y})")

    x, y = 258695, 647576
    col, row = colrow_from_xy(raster, x, y)
    print(f"Współrzędne ({x}, {y}) -> Kolumna: {col}, Wiersz: {row}")
    
    try:
        x, y = 500000, 4600000
        col, row = colrow_from_xy(raster, x, y)
        print(f"Współrzędne ({x}, {y}) -> Kolumna: {col}, Wiersz: {row}")
    except ValueError:
        print("Współrzędne poza zakresem rastra")
        
        
        
    wktPolygon = "POLYGON ((40 30, 60 30, 50 40, 40 30))"
    polygon = QgsGeometry.fromWkt(wktPolygon)
    print(polygon)
        
    x1, y1 = geometry_to_coords(polygon)
    
    rotatedPolygon = rotate(polygon, 30, 50, 33.3333333)
    print(rotatedPolygon)
    x2, y2 = geometry_to_coords(rotatedPolygon)
    
    reflectedPolygon = horizontalReflect(polygon, 30)
    print(reflectedPolygon)
    x3, y3 = geometry_to_coords(reflectedPolygon)
    

    plt.figure(figsize = (4, 3))
    plt.plot(x1, y1, color = "grey", label="Original Polygon", linestyle = "dashed", zorder = 1)
    plt.fill(x2, y2, color = "blue", label="Rotated Polygon", zorder = 3)
    plt.fill(x3, y3, color = "red", label="Reflected Polygon", zorder = 2)
    plt.legend(loc="upper left", fontsize=10)
    plt.title("Transformacje geometrii")
    plt.xlim(35, 65)
    plt.ylim(15, 45)
    plt.show()


    
main()