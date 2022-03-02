import dolphin_memory_engine as dme
import sys
import json
from . import ppc

def hook():
    if sys.platform == "win32":
        dme.hook()
        if get_id() != "RMC":
            print("Your game("+ get_id() +"X) is not supported.")
            sys.exit()
        else:
            global region
            region = get_region()
            if region != "J" and region != "E" and region != "P" and region != "K":
                print("Your region(RMC'"+ region +"') is not supported.")
                sys.exit()
    else: # On Linux/Darwin, force close
        print("Your platform("+ sys.platform +") is not supported.")
        sys.exit()


# Load Pointer
def lp(a):
    v = hex(a)[2:]
    v = int(v, 16)
    return dme.read_word(v)


# Byte Shift
def byslwi(a, bytes):
    v = hex(a << bytes*8)[bytes*2+2:]
    return  int(v, 16)

def bysrwi(a, bytes):
    v = hex(a >> bytes*8)[bytes*2+2:]
    return  int(v, 16)


def get_id():
    i = dme.read_word(int(json.load(open('symbol/rmc.json', 'r'))['GameID'][2:], 16))
    i = bytearray.fromhex(str(hex(i))[2:]).decode()[:3]
    return i

def get_region():
    r = dme.read_byte(int(json.load(open('symbol/rmc.json', 'r'))['GameRegion'][2:], 16))
    r = bytearray.fromhex(str(hex(r))[2:]).decode()
    return r


def get_pid():
    v = lp(int(json.load(open('symbol/rmc' + region.lower() + '.json', 'r'))['RaceData'], 16))
    v = ppc.lbz(v, 0xB84)
    return v

def get_address_memory_coordinate(pid):
    v = lp(int(json.load(open('symbol/rmc' + region.lower() + '.json', 'r'))['PlayerHolder'], 16))
    v = ppc.lwz(v, 0x20)
    v = ppc.lwz(v, pid*4)
    v = ppc.lwz(v, 0x0)
    v = ppc.lwz(v, 0x8)
    v = ppc.lwz(v, 0x90)
    v = ppc.lwz(v, 0x4)
    addr = v + 104
    return addr

def get_address_memory_item(pid):
    v = lp(int(json.load(open('symbol/rmc' + region.lower() + '.json', 'r'))['ItemHolder'], 16))
    v = ppc.lwz(v, 0x14)
    addr = v + pid*4 + 0x8C
    return addr