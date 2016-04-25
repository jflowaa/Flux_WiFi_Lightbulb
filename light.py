#!/usr/bin/env python
import socket


class LightControl():
    """
        This class holds all the functions for controlling
        the lightbulb. I.E. turn on, off, change color, get
        status, etc.
    """
    def __init__(self, ip, port):
        """
            Initializes all of the variables used for controlling the bulb.
            Creates a connection to the lightbulb.
        """
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, port))
        self.commands = {
                "on":  bytearray([0x71, 0x23, 0x0F]),
                "off": bytearray([0x71, 0x24, 0x0F]),
                "status": bytearray([0x81, 0x8A, 0x8B])
                }
        self.status = None
        self.poll()


    def send(self, command):
        self.sock.send(self.checksum(command))

    def checksum(self, command):
        checksum = sum(command) & 0xFF
        command.append(checksum)
        return command

    def poll(self):
        self.send(self.commands.get("status"))
        res = self.sock.recv(1024)
        print(res)
        print(res[-1:])
        if b'\x8d' == res[-1:] or b'\xa3' == res[-1:] or b'#' in res:
            self.status = "On"
            print("LightControl: on")
        if b'\x8e' == res[-1:] or b'\xa4' == res[-1:] or b'$' in res:
            self.status = "Off"
            print("LightControl: off")
    
    def get_status(self):
        return self.status

    def turn_on(self):
        self.send(self.commands.get("on"))
        self.status = "On"

    def turn_off(self):
        self.send(self.commands.get("off"))
        self.status = "Off"
    
    def change_color(self, r, g, b):
        if r + g + b == 0:
            c = bytearray([0x31, r, g, b, 0xFF, 0x0F, 0x0F])
        else:
            c = bytearray([0x31, r, g, b, 0x00, 0xF0, 0x0F])
        self.send(c)
