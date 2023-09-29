import socket
import os

def client_program():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 2000))
    ask = True    
    while ask:
        action = input("enter download for downloading, upload for uploading or stop for stoping networking\n")#why I can't input here
        client_socket.send(action.encode())
        if(action == "upload"):
            
            filename = input("enter the file name you wanna upload\n")
            file = open(filename, "rb")
            filesize = os.path.getsize(filename)
            message = f"{filename}\n{filesize}"
            client_socket.send(message.encode())
            data = file.read()
            client_socket.sendall(data)
            file.close()
            print("send")
        elif(action == "download"):
            filename = input("enter the file name you wanna download\n")
            client_socket.send(filename.encode())
            file = open(filename, "wb")
            filesize = client_socket.recv(1024).decode()
            filesize = int(filesize)
            received_bytes = 0
            while received_bytes < filesize:
                data = client_socket.recv(1024)
                if not data:
                    break  
                file.write(data)
                received_bytes += len(data)
            file.close()
            print("we got the file")


        elif(action == "stop"):
            ask = False
if _name_ == '_main_':
    client_program()