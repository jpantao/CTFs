#!/bin/python3

from pwn import *

io = remote('94.237.49.182', 35972)

delim = b'?'
flag = ''

sdr = {
    "GORGE" : "STOP",
    "PHREAK" : "DROP",
    "FIRE" : "ROLL"
}

it = 0

io.recvuntil(b"Are you ready? (y/n)")
io.sendline(b"y")
io.recvuntil(b"Ok then! Let's go!")
io.recvline()


input=''

while it < 500:
    input = io.recvline().decode().strip().split(', ')
    print(io.recvuntil(b"What do you do?").decode())
    output = '-'.join(sdr[key] for key in input)
    print(f'{input} -> {output}')
    io.sendline(output.encode())
    it+=1


io.stream()