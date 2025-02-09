'''
Oblicz długość granic i dodaj jako nowy atrybut do warstwy.
'''

import os
from qgis.core import QgsVectorLayer, QgsField
from PyQt5.QtCore import QVariant

def add_perimeter_to_layer(layer_obj, target_field_name="dl_granicy", conversion_rate=1):
    if not layer_obj.isValid():
        print("Błąd: Warstwa wektorowa jest nieprawidłowa.")
        return
        
    if not layer_obj.isEditable():
        layer_obj.startEditing()
    
    target_field_index = layer_obj.fields().indexFromName(target_field_name)
    if target_field_index == -1:
        new_attribute = [QgsField(target_field_name, QVariant.Double)]
        layer_obj.dataProvider().addAttributes(new_attribute)
        layer_obj.updateFields()
        target_field_index = layer_obj.fields().indexFromName(target_field_name)
    else:
        print(f"Pole '{target_field_name}' już istnieje. Zostanie nadpisane.")
    
    for feature_item in layer_obj.getFeatures():
        perimeter_value = feature_item.geometry().length() * conversion_rate
        layer_obj.changeAttributeValue(feature_item.id(), target_field_index, perimeter_value)
    
    layer_obj.commitChanges()
    print(f"Dodano pole '{target_field_name}' z długością granic do warstwy '{layer_obj.name()}'.")

data_directory = "/Users/michalbaczkiewicz/Documents/GitHub/adg2024/dane/"
os.chdir(data_directory)
filename = "powiaty.gpkg"
vector_layer_obj = QgsVectorLayer(filename, "powiaty", "ogr")

if vector_layer_obj.isValid():
    add_perimeter_to_layer(vector_layer_obj, conversion_rate=0.001)
else:
    print("Błąd: Nie można załadować warstwy wektorowej.")
