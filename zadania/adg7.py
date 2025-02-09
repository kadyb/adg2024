#ad7
def add_boundary_length(layer, field_name="boundary_length"):
    layer.startEditing()
    layer.dataProvider().addAttributes([QgsField(field_name, QVariant.Double)])
    layer.updateFields()
    field_index = layer.fields().indexFromName(field_name)
    for feature in layer.getFeatures():
        layer.changeAttributeValue(feature.id(), field_index, feature.geometry().length())
    layer.commitChanges()

vector_layer = QgsVectorLayer("powiaty.gpkg", "powiaty", "ogr")

add_boundary_length(vector_layer)