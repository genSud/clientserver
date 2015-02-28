#!/usr/bin/python
#coding: utf8
import socket
from sys import stdin
def main():
    sock = socket.socket()
    sock.connect(('localhost', 1111))
    while True:
        str1=stdin.readline()
        sock.send(str1)
        data = sock.recv(1024)
        print data

if __name__ == "__main__":
    main()
