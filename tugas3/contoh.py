import os
import sys as s
from pathlib import Path
from . import helper
from .util import (a, b)

def tambah(a, b):
    print("jumlah", a + b)
    return a + b

def sapa():
    print("halo")

def kali(x, y, z=1, *args, **kw):
    return x * y * z

class K:
    def m(self, n):
        print(n)
        return n