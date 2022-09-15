import csv
import json
import socket
import time
import signal
import sys

serverName = '127.0.0.1'    #localhost
serverPort = 10000

def handler(signum, frame):
    print('\nYou pressed Ctrl+C!')
    sys.exit(0)

class Money:
    def __init__(self,id,name,value1,value2):
        self.id=id
        self.name = name
        self.value1 = value1
        self.value2 = value2

signal.signal(signal.SIGINT, handler)
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as clientSocket:
    while True:
        with open("config.txt", mode='r') as file:
            for row in file:
                path = row

        #input_file = csv.DictReader(open(path))
        #list = []
        #for row in input_file:
        #    list.append(row)

        input = csv.DictReader(open(path))
        list = []
        for o in input:
            money = Money(o["id"],o["name"],o["value1"],o["value2"])
            t = {'id': money.id, 'name': money.name, 'value1': money.value1, 'value2': money.value2}
            list.append(t)
        data = json.dumps(list)

        clientSocket.sendto(data.encode(), (serverName, serverPort))
        time.sleep(30)