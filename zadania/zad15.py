#%% zad 15 - haversinus
from math import pi, cos, asin, sqrt

# lat1, lon1, lat2, lon2
def HaversineFormula(*pts):
    
    if len(pts) != 4:
        raise Exception('Funkcja przyjmuje tylko cztery punkty.')
        
    lat1,lon1,lat2,lon2 = [i * pi/180 for i in pts] # zamiana współrzędnych na radiany
    
    r_diff_lat = lat2-lat1 # różnica szerokości geog.
    r_diff_lon = lon2-lon1 # różnica długości geog.
     
    # doprowadzenie do wzoru:
    # 2r * arcsin(1 - cos(Δφ) + cos(φ_1) * cos(φ_2) * (1 - cos(ΔΛ)))
    # r - średni obwód ziemi
  
    a = ((1-cos(r_diff_lat) +
         cos(lat1) * cos(lat2) * 
         (1 - cos(r_diff_lon)))/2)
    
    rad = 6371.009 
    
    return 2 * rad * asin(sqrt(a))

pts = (52.2296, 21.0122, 41.8919, 12.5113)
HaversineFormula(*pts)
