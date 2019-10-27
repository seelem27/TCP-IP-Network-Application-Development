import http.client
import json
import csv

HOST = 'localhost'
PORT = 5000

print('### Connecting to {}:{}'.format(HOST, PORT))
conn = http.client.HTTPConnection(HOST, PORT)

print('### Sending HTTP Request')
conn.request('GET', '/api/stations')

print('### HTTP Response Received')
response = conn.getresponse()

if response.status == 200:
    stations = json.loads(response.read())

    print('### Writing CSV File')
    with open('Q2.csv', 'w', newline='') as file:
        fields = [
            'id',
            'code',
            'name',
            'type'
        ]
        writer = csv.DictWriter(file, fieldnames=fields)

        writer.writeheader()

        for station in stations:
            writer.writerow(station)

        print('### Writing Completed')

else:
    print('### ERROR: {}'.format(response.status))