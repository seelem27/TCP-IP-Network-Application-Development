import socket
import json
from datetime import datetime

PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

def getData():
    return json.dumps({
       "date_of_occurence": input("Enter date of occurence (DD/MM/YYYY): "),
        "time_of_occurence": input("Enter time of occurence (24 hours format): "),
        "warning_type": input("Enter warning type: "),
        "location": input("Enter location of occurence: "),
        "description": input("Enter description of occurence: "),
        "createdAt": str(datetime.now())
    })

if __name__ == "__main__":
    while True:
        response = getData()
        s.sendto(response.encode(), ('<broadcast>', PORT))
        print('[+] Broadcasted data to UDP port {}'.format(PORT))
        ans = input("Enter new data? (Y/N)")
        if ans == 'n':
            exit(0)

