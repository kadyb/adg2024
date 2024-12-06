vector.startEditing()

new_field = [QgsField("dl_granicy", QVariant.Double)]
vector.dataProvider().addAttributes(new_field)
vector.updateFields()

len_idx = vector.fields().indexOf("dl_granicy")

for feature in vector.getFeatures():
    length = feature.geometry().length()
    length = length / 1000
    vector.changeAttributeValue(feature.id(), len_idx, length)
    
vector.commitChanges()