import socket as sk
import random as rn
import time

IP = "192.168.1.8"
port = 12345
packet_number = 0

sock = sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
sock.bind((IP, port))

print("Connection with server started")

while True:
    sock.sendto(str(packet_number).encode(), (IP, port))
    print(f"Client sent {packet_number} to {IP}:{port}")

    data, address = sock.recvfrom(1024)
    print(f"Client received {data.decode()} from {address}")
    
    