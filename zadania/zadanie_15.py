#Zaimplementuj wzór haversine [9] jako funkcję i porównaj z innymi otrzymanymi wynikami na przykładzie odległości pomiędzy Warszawą a Rzymem.
#Współrzędne geograficzne wyrażone w stopniach muszą zostać zamienione na radiany.
import os
from math import sin, cos, asin, sqrt, pi

path = os.path.join(os.path.expanduser("~"), "Documents", "adp", "dane8")
os.chdir(path)

pt1 = (21.0122, 52.2296)
pt2 = (12.5113, 41.8919)



def dystans(pt1, pt2):
    pt1 = QgsPointXY(pt1[0], pt1[1])
    pt2 = QgsPointXY(pt2[0], pt2[1])
    r = 6371009
    
    coords = [pt1.x(), pt1.y(), pt2.x(), pt2.y()]
    coords = [coord * pi / 180 for coord in coords]
    x1, y1, x2, y2 = coords
    del1 = x2 - x1
    del2 = y2 - y1
    odl = 2*r*asin(math.sqrt((1-math.cos(del1)+math.cos(x1)*math.cos(x2)*(1-math.cos(del2)))/2))
    odl = round(odl / 1000, 2)
    return odl

odl = dystans(pt1, pt2)
print("Odległość wynosi:",odl,"km")
