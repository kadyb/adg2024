from qgis.core import QgsPointXY
from qgis.processing import alg
from processing.core.Processing import Processing
from processing.core.parameters import QgsProcessingParameterPoint
from processing.core.outputs import QgsProcessingOutputNumber

import math

@alg(name="oblicz_odleglosc_haversine", label="Oblicz odległość Haversine", group="examplescripts", group_label="Example scripts")
@alg.input(type=alg.POINT, name="punkt1", label="Punkt startowy")
@alg.input(type=alg.POINT, name="punkt2", label="Punkt końcowy")
@alg.output(type=alg.NUMBER, name="distance_km", label="Odległość (km)")
def haversine_distance_algorithm(instance, parameters, context, feedback, inputs):
    """
    Ten algorytm oblicza odległość między dwoma punktami na mapie używając formuły Haversine.
    """
    
    punkt1 = instance.parameterAsPoint(parameters, "punkt1", context)
    punkt2 = instance.parameterAsPoint(parameters, "punkt2", context)

    distance_km = haversine(punkt1.y(), punkt1.x(), punkt2.y(), punkt2.x())
    
    if feedback.isCanceled():
        return {}

    return {"Dystans między punktami w km": distance_km}


def haversine(lat1, lon1, lat2, lon2):
    R = 6371000 
    lat1_r = math.radians(lat1)
    lon1_r = math.radians(lon1)
    lat2_r = math.radians(lat2)
    lon2_r = math.radians(lon2)
    dlat = lat2_r - lat1_r
    dlon = lon2_r - lon1_r
    hav = (math.sin(dlat / 2) ** 2) + math.cos(lat1_r) * math.cos(lat2_r) * (math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(hav), math.sqrt(1 - hav))
    distance_km = round((R * c) / 1000, 2)
    return distance_km

Processing.initialize()