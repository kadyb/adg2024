#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 10:53:50 2025

@author: kuba
"""

from shapely.geometry import Polygon
from shapely import wkt
import math as m
import matplotlib.pyplot as plt


def rotacja(wkt_str, k):
    
    k = -(k * m.pi) / 180  
    
    geometry = wkt.loads(wkt_str)
    
   
    centroid = geometry.centroid
    px, py = centroid.x, centroid.y

    rotated_coords = []
    for x, y in geometry.exterior.coords:
       
        x_2 = (x - px) * m.cos(k) - (y - py) * m.sin(k) + px
        y_2 = (x - px) * m.sin(k) + (y - py) * m.cos(k) + py
        rotated_coords.append((x_2, y_2))

    rotated_polygon = Polygon(rotated_coords)
    
    
    x1, y1 = geometry.exterior.xy
    x2, y2 = rotated_polygon.exterior.xy

    
    plt.figure(figsize=(6, 6))
    plt.plot(x1, y1, color="grey", linestyle="dashed", zorder=1)  
    plt.fill(x2, y2, color="blue", alpha=0.5, zorder=2) 
    plt.scatter(px, py, color="red", zorder=3, label="Centroid")
    plt.title(f"Rotacja o {k * 180 / m.pi}°")
    plt.grid(True)
    plt.show()


polygon = "POLYGON ((40 30, 60 30, 50 40, 40 30))"
rotacja(polygon, 90)  


def przeskalowanie(wkt_str, delta_x, delta_y):

    geometry = wkt.loads(wkt_str)
    

    centroid = geometry.centroid
    px, py = centroid.x, centroid.y

    scaled_coords = []
    for x, y in geometry.exterior.coords:

        x_2 = delta_x * (x - px) + px
        y_2 = delta_y * (y - py) + py
        scaled_coords.append((x_2, y_2))


    scaled_polygon = Polygon(scaled_coords)
    

    x1, y1 = geometry.exterior.xy
    x2, y2 = scaled_polygon.exterior.xy


    plt.figure(figsize=(6, 6))
    plt.plot(x1, y1, color="grey", linestyle="dashed", zorder=1)  
    plt.fill(x2, y2, color="green", alpha=0.5, zorder=2) 
    plt.scatter(px, py, color="red", zorder=3, label="Centroid")
    plt.title(f"Przeskalowanie o Δx={delta_x}, Δy={delta_y}")
    plt.grid(True)
    plt.show()

przeskalowanie(polygon, 0.5, 0.5)

