from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import AustinHex, TrafficIncident, State
import requests
from django.contrib.gis.geos import Point, Polygon
import dateutil.parser
import csv

world_mapping = {
    'number' : 'id',
    'hex' : 'polygon',
}

def load_states():
    import requests
    resp = requests.get('https://raw.githubusercontent.com/mapbox/mapboxgl-jupyter/master/examples/data/us-states.geojson')
    data = resp.json()
    import pdb; pdb.set_trace()
    for x in data['features']:
        try:
            State.objects.get_or_create(name=x['properties']['name'], density=x['properties']['density'], shape=Polygon(x['geometry']['coordinates'][0]))
        except:
            pass

def load_hexes(verbose=True):
    world_shp = Path(__file__).resolve().parent / 'data' / 'geo_export_0aadad97-91ff-4350-8631-f1fd6e5bbf65.shp'
    lm = LayerMapping(AustinHex, str(world_shp), world_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


def load_accidents(remote=True, verbose=True):
    if remote:
        resp = requests.get('https://data.austintexas.gov/api/views/dx9v-zd7x/rows.csv?accessType=DOWNLOAD')
    else:
        traffic = Path(__file__).resolve().parent / 'data' / 'Real-Time_Traffic_Incident_Reports.csv.csv'
        with open(traffic, newline='\n') as csvfile:
            resp = csv.reader(csvfile)
        
        
    if resp.status_code == 200:
        if verbose:
            print('TRAFFIC CSV DOWNLOADED')
        reader = csv.DictReader(resp.text.strip().split('\n'))
        i = 0
        for x in reader:
            try:
                ti = TrafficIncident(
                    traffic_report_id = x['Traffic Report ID'],
                    publish_date = dateutil.parser.parse(x['Published Date']),
                    location = Point(float(x['Longitude']), float(x['Latitude'])),
                    address = x['Address'],
                    status = x['Status'],
                    status_date = dateutil.parser.parse(x['Status Date'])
                )
                ti.issue_reported = ti.get_choice(x['Issue Reported'])
                ti.save()
                
                if verbose:
                    print("{0} | {1} - SAVED".format(i, x['Issue Reported']))
                    i+=1
            except ValueError:
                if verbose:
                    print("{0} - FAILED".format(x['Issue Reported']))
    else:
        print("failed to get CSV")
        
        
def load():
    load_hexes()
    load_accidents()
