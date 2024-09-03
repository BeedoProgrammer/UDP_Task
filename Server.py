import socket as sk
import random as ran

IP = "192.168.1.8"
port = 12345
packet_number = 0

sock = sk.socket(sk.AF_INET,sk.SOCK_DGRAM)

sock.bind((IP,port))
sock.listen(5) 


while True:
    print(f"Server sending {packet_number} to {IP}:{port}")
    