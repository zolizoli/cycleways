import json
from os import listdir
from bs4 import BeautifulSoup
from os.path import isfile, join
from urllib.request import urlopen

in_path = 'data/jsons'
out_path = 'data/imgs'

fs = [f for f in listdir(in_path) if isfile(join(in_path, f))]
imgs = [f for f in listdir(out_path) if isfile(join(out_path, f))]
imgs = set([f.split('|')[0] for f in imgs])
for f in fs:
    if f.split('.')[0] not in imgs:
        print(f)
        with open(join(in_path, f), 'r') as inputfile:
            d = json.load(inputfile)
            features = d['features']
            if len(features) > 0:
                i = 0
                for feature in features:
                    img_id = feature['properties']['key']
                    base = 'https://www.mapillary.com/map/im/'
                    url = base + img_id
                    html = urlopen(url).read()
                    soup = BeautifulSoup(html)
                    links = soup.find_all('meta')
                    links = [l['content'] for l in links if l.has_attr('content')]
                    links = set([l for l in links if l.endswith('jpg')])
                    for link in links:
                        filename = f.split('.')[0] + '|' + str(i) + '.jpg'
                        response = urlopen(link).read()
                        with open(join(out_path, filename), 'wb') as outfile:
                            outfile.write(response)
                            i += 1
