import threading   
import socket

HOST = '127.0.0.1'
PORT = 12345

def handle_client(client_sock, client_addr, other_client_sock):
    print(f"ansluten till {client_addr}")
    
    while True:
        try:
            message = client_sock.recv(1024).decode('utf-8')
            if not message:
                print(f"klient frånkopplad {client_addr}")
                break
            print(f"meddelande från {client_addr}: {message} ")
            other_client_sock.sendall(f"{client_addr} säger {message}".encode('utf-8'))
            
        except ConnectionResetError:
            print(f"Anslutningen förlorad till {client_addr}")
            break             

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.bind((HOST,PORT))
        server_sock.listen(2)
        print(f"serven körs på {HOST}: {PORT}")
        print("Väntar på att 2 klienter ska ansluta för att kunna chatta med varandra!")
    
        client1_sock, addr1 = server_sock.accept()
        print(f"klient 1 är ansluten till {addr1}")
    
        client2_sock, addr2 = server_sock.accept()
        print(f"klient 2 är ansluten till {addr2}")
    
        threading.Thread(target=handle_client, args=(client1_sock, addr1, client2_sock)).start()
        threading.Thread(target=handle_client, args=(client2_sock, addr2, client1_sock)).start() 

start_server() 
        