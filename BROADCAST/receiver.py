import socket
import json

PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('', PORT))

def receiveData(title, value):
    print(f"{title} : {value}")

while True:
    data, addr = s.recvfrom(1024)
    data = json.loads(data.decode())
    receiveData("Received on: ", data['createdAt'])
    receiveData("Date of occurence: ", data['date_of_occurence'])
    receiveData("Time of occurence: ", data['time_of_occurence'])
    receiveData("Warning type: ", data['warning_type'])
    receiveData("Location of occurence: ", data['location'])
    receiveData("Description of occurence: ", data['description'])
    print('')