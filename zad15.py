# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 10:49:22 2025

@author: krzys
"""

from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):
    promien_ziemi = 6371.0  # w kilometrach
    
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    a = sin(delta_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(delta_lon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    odleglosc = round(promien_ziemi * c, 2)

    return f"Odległość: {odleglosc} km"

# Przykładowe wywołanie
print(haversine(52.2298, 21.0118, 41.902, 12.4964))
