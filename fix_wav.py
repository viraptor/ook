#!/usr/bin/env python3

import sys
import os
import struct

f = open(sys.argv[1], 'r+b')
end = f.seek(0, os.SEEK_END)

f.seek(4)
chunk_size = struct.pack("<I", end-8)
f.write(chunk_size)

f.seek(40)
chunk_size = struct.pack("<I", end-44)
f.write(chunk_size)

f.close()
