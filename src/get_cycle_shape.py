import shapefile

f = 'data/shp/roads.shp'

sf = shapefile.Reader(f)

records = sf.records()
shapeRecs = sf.shapeRecords()

# 33 categories
cats = []
for record in records:
    cats.append(record[3])
cats = set(cats)
for cat in cats:
    print(cat)

# cycleway kell csak nekünk
w = shapefile.Writer()
w.fields = sf.fields[1:]
for shaperec in sf.iterShapeRecords():
    if shaperec.record[3] == 'cycleway':
        w.record(*shaperec.record)
        w._shapes.append(shaperec.shape)
w.save('data/cycle_shp/bp.shp')
