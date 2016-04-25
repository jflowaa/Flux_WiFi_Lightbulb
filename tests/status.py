#!/usr/bin/env python
import socket
ip = "192.168.35.184"
port = 5577
on_command = bytearray([0x81, 0x8A, 0x8B])
checksum = sum(on_command) & 0xFF
on_command.append(checksum)

print("[*] IP: {}".format(ip))
print("[*] Port: {}".format(port))
print("[*] Command: {}".format(on_command))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, port))

sock.send(on_command)
data = bytearray(100)
data = sock.recv(1024)
print("[+] Response: {}".format(data))
if b'\x81D#a!' in data:
    print("On")
else:
    print("Off")
sock.close()
