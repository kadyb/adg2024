import random

def sample_strata(wektor, n, output_path):
    output_layer = QgsVectorLayer('Point?crs=' + wektor.crs().toWkt(), 'Stratyfikowane Punkty', 'memory')
    prov = output_layer.dataProvider()
    prov.addAttributes([
        QgsField('id', QVariant.Int),
        QgsField('nazwa', QVariant.String)
    ])
    output_layer.updateFields()
    for feature in wektor.getFeatures():
        geom = feature.geometry()
        if not geom.isGeosValid():
            continue
        bbox = geom.boundingBox()  
        for _ in range(n):
            while True:
                x = random.uniform(bbox.xMinimum(), bbox.xMaximum())
                y = random.uniform(bbox.yMinimum(), bbox.yMaximum())
                random_point = QgsPointXY(x, y)
                if geom.contains(QgsGeometry.fromPointXY(random_point)):
                    break
            point_feature = QgsFeature()
            point_feature.setGeometry(QgsGeometry.fromPointXY(random_point))
            point_feature.setAttributes([feature.id(), feature['nazwa'] if 'nazwa' in feature.fields().names() else None])
            prov.addFeature(point_feature)
    QgsVectorFileWriter.writeAsVectorFormat(
        output_layer,
        output_path,
        'UTF-8',
        driverName='GPKG'
    )
    print(f"Saved as {output_path}")
    return output_layer

vct = QgsVectorLayer('powiaty.gpkg', 'Powiaty', 'ogr')

strata_result = sample_strata(vct, n=5, output_path = 'wynik.gpkg')