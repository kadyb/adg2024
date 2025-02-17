#Stwórz nową warstwę z obliczonymi centroidami dla powiatów 
#i zapisz ją na dysku w formacie .gpkg.

import processing

vectorname = "powiaty.gpkg"
vector = QgsVectorLayer(vectorname)

def centroidy(vector):
    
    tp = 'TEMPORARY_OUTPUT'
    
    fix_params = {
        'INPUT': vector,
        'OUTPUT': tp
    }
    vector_fix = processing.run("native:fixgeometries", fix_params)['OUTPUT']

    cent_params = {
        'INPUT': vector_fix,
        'ALL_PARTS': True,
        'OUTPUT': tp
    }
    vector_centroidy = processing.run("native:centroids", cent_params)['OUTPUT']
    
    QgsVectorFileWriter.writeAsVectorFormat(vector_centroidy, 'centroidy.gpkg', "UTF-8")

    QgsProject.instance().addMapLayer(vector_centroidy)

centroidy(vector)
