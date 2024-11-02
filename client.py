import threading
import socket

HOST = '127.0.0.1'
PORT = 12345

def receve_message(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message:
                print(message)
        
        except ConnectionResetError:
            print("Anslutning förlorad, tryck på enter för att avsluta chatten! ")
            break
        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
    client_sock.connect((HOST, PORT))
    print("Ansluten till serven")
    
    threading.Thread(target= receve_message, args=(client_sock,)).start()
    
    while True:
        message = input(">: ")
        client_sock.sendall(message.encode('utf-8'))
