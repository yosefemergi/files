import socket
import os

def server_program():
    check = input("Enter if you want to keep the server live\n")
    while (check == "Yes"):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("127.0.0.1", 2000))
        server_socket.listen(1)
        print("before connecting")
        client, addr = server_socket.accept()
        print("It's connected")
        ask = True
        while ask:
            action = client.recv(1024).decode()
            print(action)
            if(action == "upload"):
                message = client.recv(1024).decode()
                filename, filesize = message.split('\n')
                file = open(filename, "wb")
                filesize = int(filesize)
                received_bytes = 0
                while received_bytes < filesize:
                    data = client.recv(1024)
                    if not data:
                        break  
                    file.write(data)
                    received_bytes += len(data)
                file.close()
                print("we got the file")
            elif(action == "download"):
                filename = client.recv(1024).decode()
                filesize = os.path.getsize(filename)
                client.send(str(filesize).encode())
                file = open(filename, "rb")
                data = file.read()#the read func doesn't work
                client.sendall(data)
                file.close()
                print("sent")
            elif(action == "stop"):
                ask = False
        client.close()
        check = input("Enter if you want to keep the server live\n")
    server_socket.close()


        
    
    


server_program()