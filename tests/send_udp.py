#!/usr/bin/env python
import socket

ip = "191.168.1.117"
port = 48899 
command = "HF-A11ASSISTHREAD"

print("[*] Target IP: {}".format(ip))
print("[*] Target port: {}".format(port))
print("[*] Sending: {}".format(command))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(command, (ip, port))

data, addr = sock.recvfrom(1024)
print("[+] response: {}".format(data))
