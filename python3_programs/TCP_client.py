import socket

target_host = str(input("Enter target Host: "))
target_port = int(input("Enter target Port: "))

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host,target_port))

data_out = "GET / HTTP/1.1\r\nHost: {0}\r\n\r\n".format(target_host).encode()

# send some data
client.send(data_out)

# recive some data
response = client.recv(4096)

# changes byte-type information to fromatable string for outputing
respon = response.decode()

print("")
print("####################################################################")
print("")
print(respon)
