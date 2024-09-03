import socket as sk
import random as rn

server_IP = "192.168.1.8"
server_port = 12345
packet_number = 0

sock = sk.socket(sk.AF_INET,sk.SOCK_DGRAM)

sock.bind((server_IP,server_port))
sock.listen(5) 

print("Server connection started")

while True:
    client_sock, client_IP, client_packetNum = sock.accept()
    data = client_sock.recv(1024)

    print(f"Server received {client_packetNum} from {client_IP}:{client_sock}:")
    print(data.decode())
    client_sock.send(f"Server sending {packet_number} to {client_IP}:{client_sock}".encode())
    packet_number = packet_number + 1

    client_sock.close()
    print(f"connection with {client_IP}:{client_sock} ended")