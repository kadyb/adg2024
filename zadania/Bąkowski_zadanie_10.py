import os
from qgis.core import *
from qgis.gui import *
from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
from qgis.PyQt.QtCore import QVariant

# Inicjalizacja QGIS
QgsApplication.setPrefixPath("/usr", True)
qgs = QgsApplication([], False)
qgs.initQgis()

# Ustawienie ścieżki roboczej
default_path = os.path.join(os.path.expanduser("~"), "Documents")
os.chdir(default_path)
data_folder = os.path.join(default_path, "Wlasne")

# Ścieżki do danych
pan_path = os.path.join(data_folder, "LC08_L1TP_011019_20241219_20241219_02_RT_B8.tif")  # Kanał panchromatyczny
blue_path = os.path.join(data_folder, "LC09_L2SP_016037_20241214_20241215_02_T1_SR_B2.tif")  # Kanał niebieski
green_path = os.path.join(data_folder, "LC09_L2SP_016037_20241214_20241215_02_T1_SR_B3.tif")  # Kanał zielony
red_path = os.path.join(data_folder, "LC09_L2SP_016037_20241214_20241215_02_T1_SR_B4.tif")  # Kanał czerwony

# Ścieżka wyjściowa dla wyniku
output_path = os.path.join(default_path, "output_pansharpened.tif")

# Wczytanie rastrów
pan_layer = QgsRasterLayer(pan_path, "Panchromatic")
red_layer = QgsRasterLayer(red_path, "Red")
green_layer = QgsRasterLayer(green_path, "Green")
blue_layer = QgsRasterLayer(blue_path, "Blue")

if not pan_layer.isValid() or not red_layer.isValid() or not green_layer.isValid() or not blue_layer.isValid():
    print("One or more raster layers are invalid!")
    exit()

# Funkcja do wykonania pansharpeningu
# Function to perform pansharpening
def pansharpen(pan_layer, spectral_layer, output_file):
    entries = []

    try:
        # Panchromatic band
        pan = QgsRasterCalculatorEntry()
        pan.ref = f'{pan_layer.name()}@1'
        pan.raster = pan_layer
        pan.bandNumber = 1
        entries.append(pan)

        # Spectral band
        band = QgsRasterCalculatorEntry()
        band.ref = f'{spectral_layer.name()}@1'
        band.raster = spectral_layer
        band.bandNumber = 1
        entries.append(band)

        # Formula for pansharpening
        formula = f'(({pan.ref} + {band.ref}) / 2)'

        # Raster calculator
        calc = QgsRasterCalculator(
            formula,
            output_file,
            'GTiff',
            pan_layer.extent(),
            pan_layer.width(),
            pan_layer.height(),
            entries
        )

        result = calc.processCalculation()

        if result == QgsRasterCalculator.Success:
            print(f"Pansharpening completed for {spectral_layer.name()} and saved to {output_file}")
        else:
            print(f"Failed to process pansharpening for {spectral_layer.name()}")
    except Exception as e:
        print(f"Error during pansharpening: {e}")

# Tworzenie rastrów pansharpened dla kanałów R, G, B
red_pansharpened_path = os.path.join(default_path, "output_red.tif")
green_pansharpened_path = os.path.join(default_path, "output_green.tif")
blue_pansharpened_path = os.path.join(default_path, "output_blue.tif")

pansharpen(pan_layer, red_layer, red_pansharpened_path)
pansharpen(pan_layer, green_layer, green_pansharpened_path)
pansharpen(pan_layer, blue_layer, blue_pansharpened_path)

# Łączenie kanałów R, G, B w jedną kompozycję RGB
try:
    processing.run(
        "gdal:merge", {
            'INPUT': [red_pansharpened_path, green_pansharpened_path, blue_pansharpened_path],
            'PCT': False,
            'SEPARATE': False,
            'NODATA_INPUT': None,
            'NODATA_OUTPUT': None,
            'OPTIONS': '',
            'EXTRA': '',
            'DATA_TYPE': 6,  # Float32
            'OUTPUT': output_path
        }
    )
    print(f"Final RGB pansharpened image saved at {output_path}")
except Exception as e:
    print(f"Error during merging: {e}")

# Czyszczenie QGIS
del pan_layer
del red_layer
del green_layer
del blue_layer
qgs.exitQgis()

