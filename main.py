import jsonlines
import requests
import datetime
import time

### Very simple implementation but might be interesting in future for further analysis
### Requires you to be logged in ICE Wifi

TRIP_URL = 'https://iceportal.de/api1/rs/tripInfo/trip'
STATUS_URL = 'https://iceportal.de/api1/rs/status'

## Function to retrieve a json object from a URL
def get_json_from_url(url):
    try:
        req = requests.get(url)
    except Exception as e:
        return {'error': str(e)}
    return req.json()

## Do one initial trip request to get information about the trip for better file naming
trip_data = get_json_from_url(TRIP_URL)['trip']
now = datetime.datetime.now()
file_name = now.strftime("%Y-%m-%d %H.%M") + f'_{trip_data["trainType"]}{trip_data["vzn"]}_{trip_data["stops"][0]["station"]["name"]}-{trip_data["stops"][len(trip_data["stops"])-1]["station"]["name"]}.jsonlines'
# example for file_name: 2019-05-22 21:06_ICE635_Bremen Hbf-Nürnberg Hbf.jsonlines
print(f'Logging to: {file_name}')

fp = open(file_name, 'w', encoding='utf-8')
jsonlines_writer = jsonlines.Writer(fp, flush=True)

while True:
    time.sleep(3) # Data gets refreshed about every 3 seconds

    trip_data = get_json_from_url(TRIP_URL)
    status_data = get_json_from_url(STATUS_URL)
    complete_data = {'trip': trip_data, 'status': status_data, 'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}

    jsonlines_writer.write(complete_data)
