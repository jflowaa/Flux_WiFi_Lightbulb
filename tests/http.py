#!/usr/bin/env python
import socket

ip = "114.215.135.59"
port = 80
sock = socket.socket()
sock.connect((ip, port))

http = """
            POST /WebMagicHome/ZenggeCloud/AB003.ashx HTTP/1.1
            Content-Type: application/x-www-form-urlencoded;charset=UTF-8
            Accept-Charset: UTF-8
            zg-app-cmd: DataCommand
            User-Agent: Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus 5 Build/MOB30D)
            Host: wifi.magichue.net
            Connection: Keep-Alive
            Accept-Encoding: gzip
            Cookie: .ASPXAUTH=EFE006BA16B9C4E3E64E6963F778F27893B8B4BAE83A6966C12DE84CDBC0719455F99B510F717AA5A17CB07A29DFF2D8D397163E80E0DD5B47B7A22621845AE797DC39BD4BB3A1A9E704B216E4099D53796C9E2A70855E6352FC4BC2C9D3B8C84810F186A5380A4B734971DC223C2B0B65BBAF35DE0688DAA8980F1FB0379CFA7FE94AB31FEC7E020CE721516FC8B96787D5AE197493FDC1043CE0783EC753A5 
            Content-Length: 58
            Data=81+8a+8b+96+&ResponseCount=14&MacAddress=ACCF237FEF10
        """

data = bytearray()
data.extend(map(ord, http))


sock.send(data)
print(sock.recv(1024))



