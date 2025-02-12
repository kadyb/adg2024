from math import *

# zad 15 Zaimplementuj wzór haversine [9] jako funkcję i porównaj z innymi otrzymanymi wynikami na przykładzie odległości pomiędzy Warszawą a Rzymem. Współrzędne geograficzne wyrażone w stopniach muszą zostać zamienione na radiany.

def haversine(punkt1, punkt2):
    r = 6371
    rad_x1, rad_y1 = radians(punkt1[0]), radians(punkt1[1])
    rad_x2, rad_y2 = radians(punkt2[0]), radians(punkt2[1])
    roz_szer = rad_x2 - rad_x1
    roz_dl = rad_y2 - rad_y1
    odlegosc = 2 * r * asin(sqrt((1 - cos(roz_szer) + cos(rad_x1)*cos(rad_x2) * (1 - cos(roz_dl)))/2))
    return odlegosc

warszawa = (52.2296, 21.0122)
rzym = (41.8919, 12.5113)

haversine(warszawa,rzym)
