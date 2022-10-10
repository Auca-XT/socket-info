#!/usr/bin/python
# coding=utf-8

import socket
import nmap

web = input("enter url: ")

webadress = (socket.gethostbyname("www." + web,))

print('\n' + webadress, '\n' )

nm = nmap.PortScanner()
print(nm.nmap_version())
nm.scan(webadress, '1-1024', '-v')
print(nm.scaninfo())
print(nm.csv())