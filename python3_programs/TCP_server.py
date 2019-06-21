import socket, threading

try:
    bind_ip = "0.0.0.0"
    bind_port = 9999

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((bind_ip, bind_port))

    server.listen(5)

    print("[*] Listening on {0}, port: {1}".format(bind_ip, bind_port))

    def handle_client(client_socket):
        tester = 0
        while tester == 0:

            request = client_socket.recv(1024)
            request = request.decode()
            
            if request == "Quit":
                tester = 1
                print('[*] Client Disconnected!') 
            else:
                print('[*] Message: {0}'.format(request))

                client_socket.send(b"[*] Recived:")

    while True:
        client, addr = server.accept()
        print('[*] Accepted Connection From: {0}:{1}'.format(addr[0],addr[1]))

        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
        
except:
    client.close()
    print('[*] Shutting Down Server.')
