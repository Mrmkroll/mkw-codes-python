import dolphin_memory_engine as dme 

# Load Immediate
def li(a):
    v = hex(a)[2:6]
    return int(v, 16)

def lis(a):
    v = hex(a)[2:6] + "0000"
    return int(v, 16)


# Load and Zero
def lwz(addr, b):
    v = dme.read_word(addr+b)
    return v

def lhz(addr, b):
    v = dme.read_bytes(addr+b, 2)
    return int.from_bytes(v, 'big')

def lbz(addr, b):
    v = dme.read_byte(addr+b)
    return v


# Store
def stw(addr, b, c):
    dme.write_word(addr+b, c)

def sth(addr, b, c):
    c = hex(c)[2:]
    c = int(c[-4:], 16)
    c = c.to_bytes(2, "big")
    dme.write_bytes(addr+b, c)

def stb(addr, b, c):
    c = hex(c)[2:]
    c = int(c[-2:], 16)
    dme.write_byte(addr+b, c)


# OR Immediate
def ori(a, b):
    a = hex(a)[2:]
    b = hex(b)[2:]
    return int(a[:-len(b)]+b, 16)

def oris(a, b):
    k = hex(a)[2:6]
    l = hex(b)[2:] + "0000"
    return int(l[:-len(k)]+k, 16)


# Not
def NOT(a):
    v = hex(0xFFFFFFFF - a)
    return int(v, 16)


# Load String Word Immediate
def lswi(addr, bytes):
    if bytes == 8:
        addr = dme.read_bytes(addr, 8)
        k = int.from_bytes(addr[:4], "big")
        l = int.from_bytes(addr[4:8], "big")
        return k, l
    elif bytes == 12:
        addr = dme.read_bytes(addr, 12)
        k = int.from_bytes(addr[:4], "big")
        l = int.from_bytes(addr[4:8], "big")
        m = int.from_bytes(addr[8:12], "big")
        return k, l, m
    elif bytes == 16:
        addr = dme.read_bytes(addr, 16)
        k = int.from_bytes(addr[:4], "big")
        l = int.from_bytes(addr[4:8], "big")
        m = int.from_bytes(addr[8:12], "big")
        n = int.from_bytes(addr[12:16], "big")
        return k, l, m, n


# Store String Word Immediate
def stswi(addr, bytes, k, l, m=None, n=None):
    if bytes == 8:
        v = k.to_bytes(4, "big") + l.to_bytes(4, "big")
    elif bytes == 12:
        v = k.to_bytes(4, "big") + l.to_bytes(4, "big") + m.to_bytes(4, "big")
    elif bytes == 16:
        v = k.to_bytes(4, "big") + l.to_bytes(4, "big") + m.to_bytes(4, "big") + n.to_bytes(4, "big")
    dme.write_bytes(addr, v)


# Shift Immediate
def slwi(a, bit):
    v = hex(a << bit)
    return  int(v, 16)


def srwi(a, bit):
    v = hex(a >> bit)
    return  int(v, 16)