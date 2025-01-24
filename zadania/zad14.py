import os
import qgis.core as qc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = os.path.join(os.path.expanduser('~'),'algorytmy_geo')
os.chdir(path)


def DecimalToDMS(coords, v_lvl = True):
    if coords == 0:
        res = str(coords) + '°'
        return res
    if coords > 0:
        if v_lvl is True:
            w_dir = 'N'
        else:
            w_dir = 'E'
    if coords < 0:
        if v_lvl is True:
            w_dir = 'S'
        else:
            w_dir = 'W'
    minutes = round(coords - int(coords),len(str(coords))) * 60
    seconds = round(minutes - int(minutes),len(str(minutes))) * 60
    res = str(abs(int(coords))) + "°" + str(abs(int(minutes))) + "'" + str(abs(seconds)) + "\"" + w_dir
    return res 

# przykłady
dms = DecimalToDMS(52.2928)
dms2 = DecimalToDMS(-17.63582,False)
dms0 = DecimalToDMS(0)
