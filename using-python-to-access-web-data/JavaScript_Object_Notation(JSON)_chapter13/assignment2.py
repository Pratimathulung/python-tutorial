import urllib.request, urllib.parse
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

def get_place_id():
    address = input('Enter location: ')
    if len(address) < 0:
        return

    url = serviceurl + urllib.parse.urlencode({'sensor': 'false', 'address': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    if 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        return

    place_id = js['results'][0]['place_id']
    return place_id

place_id = get_place_id()

print('The place ID is:', place_id)
