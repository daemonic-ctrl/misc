import socket

target_host = str(input('Enter Host: '))
target_port = int(input('Enter port: '))



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

while True:
    info = input('Enter Message: ')
    infomo = info.encode()
    client.send(infomo)

    response = client.recv(4096)
    respon = response.decode()
    print(respon)

