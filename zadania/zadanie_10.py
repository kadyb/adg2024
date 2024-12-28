import os
from osgeo import gdal, ogr, osr

path = os.path.join(os.path.expanduser("~"), "Documents", "dane")
os.chdir(path)

f_red = "landsat/LC08_L1TP_189024_20241202_20241209_02_T1_B2.tif"
f_green = "landsat/LC08_L1TP_189024_20241202_20241209_02_T1_B3.tif"
f_blue = "landsat/LC08_L1TP_189024_20241202_20241209_02_T1_B4.tif"
f_panchr = "landsat/LC08_L1TP_189024_20241202_20241209_02_T1_B8 (1).tif"

# resampling 
red = gdal.Open(f_red)
red_resampled = gdal.Warp("red_resampled.tif", red, format = "GTIFF",
xRes = 15, yRes = 15, srcSRS = red.GetSpatialRef(), dstSRS = "EPSG:2180",
resampleAlg = 0)
red = None

green = gdal.Open(f_green)
green_resampled = gdal.Warp("green_resampled.tif", green, format = "GTIFF",
xRes = 15, yRes = 15, srcSRS = green.GetSpatialRef(), dstSRS = "EPSG:2180",
resampleAlg = 0)
green = None

blue = gdal.Open(f_blue)
blue_resampled = gdal.Warp("blue_resampled.tif", blue, format = "GTIFF",
xRes = 15, yRes = 15, srcSRS = blue.GetSpatialRef(), dstSRS = "EPSG:2180",
resampleAlg = 0)
blue = None

panchr = gdal.Open(f_panchr)
panchr_resampled = gdal.Warp("panchr_resampled.tif", panchr, format = "GTIFF",
xRes = 15, yRes = 15, srcSRS = panchr.GetSpatialRef(), dstSRS = "EPSG:2180", 
resampleAlg = 0)
panchr = None

# przycięcie
projwin = (436135, 502097, 457287, 464413)

red_clipped = gdal.Translate("red_resampled_clipped.tif", "red_resampled.tif", projWin = projwin)
green_clipped = gdal.Translate("green_resampled_clipped.tif", "green_resampled.tif", projWin = projwin)
blue_clipped = gdal.Translate("blue_resampled_clipped.tif", "blue_resampled.tif", projWin = projwin)
panchr_clipped = gdal.Translate("panchr_resampled_clipped.tif", "panchr_resampled.tif", projWin = projwin)

# pansharpening - uśrednić wartości
red_psh = (red_clipped.ReadAsArray() + panchr_clipped.ReadAsArray()) / 2
green_psh = (green_clipped.ReadAsArray() + panchr_clipped.ReadAsArray()) / 2
blue_psh = (blue_clipped.ReadAsArray() + panchr_clipped.ReadAsArray()) / 2

bands = [red_psh, green_psh, blue_psh]

red_clipped = None
green_clipped = None
blue_clipped = None
panchr_clipped = None

# zapis
import numpy as np 
rgb = np.stack([red_psh, green_psh, blue_psh], axis = 0)

red = gdal.Open("red_resampled_clipped.tif")

datatype = red.GetRasterBand(1).DataType
driver = gdal.GetDriverByName("GTIFF")
size = rgb.shape
gtr = red.GetGeoTransform()
nodata = -999
ref = red.GetSpatialRef()

raster = driver.Create("zadanie_10.tif", size[2], size[1], size[0], datatype)
raster.SetGeoTransform(gtr)
raster.SetSpatialRef(ref)

for i in range(size[0]):
    band = raster.GetRasterBand(i+1)
    band.WriteArray(rgb[i, :, :])
    
raster = None