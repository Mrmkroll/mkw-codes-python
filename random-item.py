from lib import fun as fn
from lib import ppc

fn.hook()

addr = fn.get_address_memory_item(fn.get_pid())

while True:
    for item in range(19):
        ppc.stw(addr, 0, item)
        if item == 5 or 16 <= item <= 18:
            ppc.stw(addr, 4, 3)
        else:
            ppc.stw(addr, 4, 1)