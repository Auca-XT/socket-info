# coding=utf-8
import socket
web = input("enter url: ")
print('The socket info / ip adres of', web, 'is:''\n')
print(socket.gethostbyname("www." + web,))