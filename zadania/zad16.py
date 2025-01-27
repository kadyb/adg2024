import os
import qgis.core as qc
from math import sqrt

def SurfaceDistance(v,a,b):
    f1 = csv_file.getFeature(a)
    f2 = csv_file.getFeature(b)
    
    crs = qc.QgsCoordinateReferenceSystem("EPSG:2180")
    dest_crs = qc.QgsCoordinateReferenceSystem("EPSG:2177")
    trans_context = qc.QgsCoordinateTransformContext()
    transform = qc.QgsCoordinateTransform(crs, dest_crs, trans_context)
    
    pt1 = qc.QgsVector3D(round(float(f1[1]),2), round(float(f1[2]),2), round(float(f1[3]),2))
    pt2 = qc.QgsVector3D(round(float(f2[1]),2), round(float(f2[2]),2), round(float(f2[3]),2))
    pt1 = transform.transform(pt1)
    pt2 = transform.transform(pt2)
    
    return round(sqrt(abs(
            pow(pt2.x() - pt1.x(),2) +
            pow(pt2.y() - pt1.y(),2) + 
            pow(pt2.z() - pt1.z(),2)
            )),2)
    
path = os.path.join(os.path.expanduser('~'),'algorytmy_geo')
os.chdir(path)
csv_path = os.path.join(path, 'dane','profil.csv')
csv_file = qc.QgsVectorLayer(csv_path)

dist = SurfaceDistance(csv_file,1,2) # 515.79 m jeżeli zastosowany zostanie epsg:2180
dist2 = SurfaceDistance(csv_file,21,37)
