import os
from qgis.core import QgsRasterLayer
import matplotlib.pyplot as plt
import numpy as np

path = r"C:\Users\jmpos\Desktop\adp"
B1 = "LC08_L2SP_190024_20241022_20241029_02_T1_SR_B1.TIF"
B2 = "LC08_L2SP_190024_20241022_20241029_02_T1_SR_B2.TIF"
B1 = QgsRasterLayer(os.path.join(path, B1),"b1")
B2 = QgsRasterLayer(os.path.join(path, B2),"b2")


params_random = {
    'EXTENT': B1,
    'POINTS_NUMBER': 1000,
    'OUTPUT': 'memory:'
}

points_random = processing.run("native:randompointsinextent", params_random)['OUTPUT']

def rand_sample_raster(vector_layer, raster_layer):
    params_sampling ={
        'INPUT': vector_layer,
        'RASTERCOPY': raster_layer,
        'COLUMN_PREFIX': (str(raster_layer.name())+ '_'),
        'OUTPUT': 'memory:'
    }
    
    points_sampled = processing.run("native:rastersampling", params_sampling)
    return points_sampled['OUTPUT']

points = rand_sample_raster(points_random, B1)
points = rand_sample_raster(points, B2)

feature_count = points.featureCount()

x_values = []
y_values = []

for i in range(1, feature_count):
    feature = points.getFeature(i)
    if feature['b1_1'] != None and feature['b2_1'] != None:
        x_values.append(feature['b1_1'])
        y_values.append(feature['b2_1'])



plt.scatter(x_values, y_values, alpha=0.1)
plt.plot([0, 20000], [0, 20000], 'k--')
plt.xlabel('B1')
plt.ylabel('B2')
plt.title('Profile')
plt.xlim(min(x_values),max(x_values))
plt.ylim(min(y_values),max(y_values))
plt.show()

diff = []
for x,y in zip(x_values,y_values) :
    diff.append(x - y)


print('Średnia:',np.mean(diff))
print('Odchylenie st:',np.std(diff))
print('Mediana:',np.median(diff))

