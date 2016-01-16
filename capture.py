#!/usr/bin/env python

import socket
import binascii

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 52001))
with open('capture.data', 'ba') as f:
    while True:
        packet = s.recv(50)
        if len(packet) != 11:
            print('weird packet')
            continue
        print(binascii.hexlify(packet))
        f.write(packet)
