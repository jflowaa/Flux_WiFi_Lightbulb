#!/usr/bin/env python
import socket


ip = "192.168.35.184"
port = 5577
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, port))

commands = {
        "on":  bytearray([0x71, 0x23, 0x0F]),
        "off": bytearray([0x71, 0x22, 0x0F]),
        "warm": bytearray([0x31, 0x00, 0x00, 0x00, 0xFF, 0x0F, 0x0F]),
        "blue": bytearray([0x31, 0x00, 0x00, 0xFF, 0xFF, 0xF0, 0x0F]),
        "green": bytearray([0x31, 0x00, 0xFF, 0x00, 0xFF, 0xF0, 0x0F]),
        "red": bytearray([0x31, 0xFF, 0x00, 0x00, 0xFF, 0xF0, 0x0F])
        }


def run():
    print("List of commands:")
    for key, value in commands.items():
        print(key)
    while True:
        c = input("Command: ")
        if c not in commands:
            print("List of commands:")
            for key, value in commands.items():
                print(key)
        else:
            send(commands.get(c))

def checksum(command):
    checksum = sum(command) & 0xFF
    command.append(checksum)
    return command

def send(command):
    command = checksum(command)
    sock.send(command)

def finish():
    sock.close()


if __name__ == "__main__":
    run()
