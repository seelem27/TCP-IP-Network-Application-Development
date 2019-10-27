import http.client
import json
import csv

HOST = 'localhost'
PORT = 5000

print('### Connecting to {}:{}'.format(HOST, PORT))
conn = http.client.HTTPConnection(HOST, PORT)

with open('Q1.csv') as file:
    stations = csv.DictReader(file)
    for station in stations:
        station = dict(station)

        print('### Sending HTTP Request')
        conn.request('POST', '/api/stations', json.dumps(station), {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        })

        print('### HTTP Response Received')
        response = conn.getresponse()

        if response.status == 201:
            result = json.loads(response.read())
            print(result)
        else:
            print('### ERROR: {}'.format(response.status))