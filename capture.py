#!/usr/bin/env python

import socket
import binascii
import crcmod

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 52001))

crc = crcmod.mkCrcFun(0x131, 0xff, False)

WIND = ("N", "NNE", "NE",
        "ENE", "E", "ESE",
        "SE", "SSE", "S", "SSW", "SW",
        "WSW", "W", "WNW",
        "NW", "NNW")

with open('capture.data', 'ba') as f:
    while True:
        packet = s.recv(32)
        if len(packet) != 11:
            continue
        if packet[0] != 0xff:
            continue
        cs = crc(packet[:-1])
        if packet[-1] != cs:
            print('checksum fail')
            continue
        print("temp  = %.1f°C" % (((packet[2]&0x0f)*0x100 + packet[3] - 0x190)*0.1))
        print("hum   = %.i%%" % packet[4])
        try:
            print("dir   = %s" % WIND[packet[9] % 0x0f])
        except:
            print("dir   = ?")
        print("speed = %.1f km/h" % packet[5])
        print("unkn  = %02x ... %02x %02x %02x" % (packet[1], packet[6], packet[7], packet[8]))
        f.write(packet)
