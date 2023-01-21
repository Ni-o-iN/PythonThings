import json
from pprint import pprint as pp

#öffnen der Datei
#f = open('golf.json')
#gibt json als ein dictionary zurück
#golfDS = json.load(f)
#pp(golfDS)


d = open('titanic.json')
titanicDS = json.load(d)
pp(titanicDS)