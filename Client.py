import socket as sk
import random as rn

client_IP = "192.168.1.8"
client_port = 12345
packet_number = 0

sock = sk.socket(sk.AF_INET,sk.SOCK_DGRAM)