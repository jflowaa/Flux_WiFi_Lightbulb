#!/usr/bin/env python
import socket
ip = "192.168.35.184"
port = 5577
on_command = bytearray([0x71, 0x24, 0x0F])
checksum = sum(on_command) 
on_command.append(checksum)

print("[*] IP: {}".format(ip))
print("[*] Port: {}".format(port))
print("[*] Command: {}".format(on_command))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, port))

sock.send(on_command)
data = sock.recv(1024)
print("[+] Response: {}".format(data))
sock.close()
