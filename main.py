# coding=utf-8
import socket
import nmap
web = input("enter url: ")

webadress = (socket.gethostbyname("www." + web,))

print('\n' + webadress, '\n' )