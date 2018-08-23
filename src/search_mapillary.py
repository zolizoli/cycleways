import json
import requests
import shapefile
from os.path import join

client_id = 'OG1ybGctcElmREk1ZE5EWVpLY29LQTpmOWJlMWE4YTViZDQ3YTIz'


def search(bounding_box):
    msg = """https://a.mapillary.com/v3/images?client_id=%s&bbox=%s""" % (client_id, bounding_box)
    response = requests.get(msg)
    return response.json()

f = 'data/cycle_shp/bp.shp'
sf = shapefile.Reader(f)

records = sf.records()
shapeRecs = sf.shapeRecords()
out_path = 'data/jsons'
for record in shapeRecs:
    rec = record.record
    bbox = record.shape.bbox
    bbox = [str(point) for point in bbox]
    fname = '_'.join(bbox).replace('.', ',') + '.json'
    print(fname)
    bbox = ','.join(bbox)
    res = search(bbox)
    with open(join(out_path, fname), 'w') as f:
        json.dump(res, f)
