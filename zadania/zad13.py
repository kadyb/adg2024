#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import qgis.core as qc
import sys
from PyQt5.QtWidgets import QApplication
import random
app = QApplication(sys.argv)

path = os.path.join(os.path.expanduser('~'),'algorytmy_geo') # wg swoich potrzeb
os.chdir(path)
path_data = os.path.join(path,'dane')

def SampleStratif(vect, n):
    new_vect = qc.QgsVectorLayer('point','pt_stratified','memory')
    new_vect.setCrs(vect.crs())
    feats = vect.getFeatures()
    random.seed(48214)
    for feature in feats:
        bbox = feature.geometry().boundingBox()
        t = 0
        while t < n:
            new_feat = qc.QgsFeature()
            x = bbox.xMinimum() + bbox.width() * random.random()
            y = bbox.yMinimum() + bbox.height() * random.random()
            pt = qc.QgsGeometry().fromPointXY(qc.QgsPointXY(x,y))
            if pt.within(feature.geometry()) == True:
                new_feat.setGeometry(pt)
                new_vect.dataProvider().addFeature(new_feat)
                t += 1
    new_vect.updateExtents()
    return new_vect
    

def SaveVectLayer(vect, path):
    options = qc.QgsVectorFileWriter.SaveVectorOptions()
    options.driverName = 'gpkg'
    options.fileEncoding = 'utf-8'
    options.layerName = 'stratified points'
    write = qc.QgsVectorFileWriter.writeAsVectorFormatV3(vect,path, 
                                   qc.QgsCoordinateTransformContext(),options)
    return write


vect = qc.QgsVectorLayer(os.path.join(path_data, 'powiaty.gpkg'))
n = 30
save_path = "dane/stratif_pt2.gpkg"
sample_pt = SampleStratif(vect, n)     
SaveVectLayer(sample_pt,save_path)
