#!/bin/python3

from pwn import *

io = remote('94.237.48.117', 54381)

delim = b'index:'
flag = ''
flag_len = 104

idx = 0

while idx < flag_len:
    io.sendlineafter(delim, f'{idx}'.encode())
    flag += (io.recvline().decode())[-2]
    idx += 1

print(f'flag: {flag}')