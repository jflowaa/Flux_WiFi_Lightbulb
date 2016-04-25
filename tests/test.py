#!/usr/bin/env python
import socket
ip = "192.168.1.117"
port = 5577
command = bytearray([0x31, 0x00, 0xFF, 0x00, 0xFF, 0x0F, 0x0F])
checksum = sum(command) & 0xFF
command.append(checksum)

print("[*] IP: {}".format(ip))
print("[*] Port: {}".format(port))
print("[*] Command: {}".format(command))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, port))

sock.send(command)
data = sock.recv(1024)
print("[+] Response: {}".format(data))
sock.close()
