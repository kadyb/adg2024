import os
import qgis.core as qc
from math import sqrt

def SurfaceDistance(v):
    if not v.isValid():
        raise Exception('Nieprawidłowy plik')
    sum_dist = 0
    crs = qc.QgsCoordinateReferenceSystem("EPSG:2180")
    dest_crs = qc.QgsCoordinateReferenceSystem("EPSG:2177")
    trans_context = qc.QgsCoordinateTransformContext()
    transform = qc.QgsCoordinateTransform(crs, dest_crs, trans_context)
    for f in range(1,v.featureCount()-1):
        f1 = csv_file.getFeature(f)
        f2 = csv_file.getFeature(f+1)
                
        pt1 = qc.QgsVector3D(float(f1[1]), float(f1[2]), float(f1[3]))
        pt2 = qc.QgsVector3D(float(f2[1]), float(f2[2]), float(f2[3]))
        pt1 = transform.transform(pt1)
        pt2 = transform.transform(pt2)
        
        sum_dist += sqrt(
                pow(pt2.x() - pt1.x(),2) +
                pow(pt2.y() - pt1.y(),2) + 
                pow(pt2.z() - pt1.z(),2)
                )
        
    return sum_dist
    
path = os.path.join(os.path.expanduser('~'),'algorytmy_geo')
os.chdir(path)

csv_path = os.path.join(path, 'dane','profil.csv')
csv_file = qc.QgsVectorLayer(csv_path)

dist = SurfaceDistance(csv_file)
