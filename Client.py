import socket as sk
import time

IP = "192.168.1.4"
port = 12345
packet_number = 0

sock = sk.socket(sk.AF_INET,sk.SOCK_DGRAM)

print("Connection with server started\n")

while True:
    sock.sendto(str(packet_number).encode(), (IP, port))
    print(f"Client sent {packet_number} to {IP}:{port}")

    data, address = sock.recvfrom(1024)
    print(f"Client received {data.decode()} from {address}")
    
    if int(data.decode()) == packet_number:
        packet_number = packet_number + 1
        sock.sendto(str(packet_number).encode(), address)
        print("Packet sent successfully")
        print("________________________\n")
        time.sleep(1)
    else:
        sock.sendto(str(packet_number).encode(), address)
        print("Invalid packet. Requesting again")
        print("________________________\n")
        time.sleep(1)