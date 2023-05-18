import socket
import threading
import random

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(('localhost', random.randint(8000, 9000)))

name = input('Name: ')

def receive():
    while True:
        try:
            message, _ = client.recvfrom(1024)
            print(message.decode())
        except:
            pass

thread = threading.Thread(target=receive)
thread.start()

client.sendto(f'SIGNUP:{name}'.encode(), ('localhost', 9001))

while True:
    message = input('')
    if message == '!q':
        exit()
    else:
        client.sendto(f'{name}: {message}'.encode(), ('localhost', 9001))