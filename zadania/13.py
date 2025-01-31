import os
from qgis.core import QgsVectorLayer
from qgis.core import QgsProject

path = r"C:\Users\jmpos\Desktop\adp"
powiaty = QgsVectorLayer(os.path.join(path, 'powiaty.gpkg'),"powiaty")


def sample_strata(wektor, n):
    
    QgsProject.instance().addMapLayer(wektor)
    params_random = {
        'INPUT': None,
        'POINTS_NUMBER':n,
        'OUTPUT':'TEMPORARY_OUTPUT'
        }
    
    points = QgsVectorLayer('point',"points", "memory")
    params_join = {
        'LAYERS':None,
        'OUTPUT':'TEMPORARY_OUTPUT'}
    
    for i in range(1, wektor.featureCount()+1):
        wektor.selectByIds([i])
        params_random['INPUT'] = QgsProcessingFeatureSourceDefinition(wektor.name(), selectedFeaturesOnly=True)
        random_points = processing.run("qgis:randompointsinlayerbounds", params_random)['OUTPUT']
        wektor.removeSelection()
        params_join['LAYERS'] = [points,random_points]
        points = processing.run("native:mergevectorlayers", params_join)['OUTPUT']
    
    QgsProject.instance().addMapLayer(points)
    
    return points


sample_strata(powiaty,10)
# !!! dla powiatu Krotoszyńskiego nie powstają punkty z powodu błędnej geometrii
