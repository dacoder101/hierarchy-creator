# Hierarchy Creator by dacoder101
# hierarchy.py

# Imports

from func import Menu as m
from func import Function as f
from func import Hierarchy

from os import listdir as lsDir
from os import mkdir as mkDir
from os import system as sys
import os

from console.utils import wait_key as key
from console import fx

# Setup


def cls():
    sys('clear')


if "HierarchyCreator" not in lsDir():
    mkDir("HierarchyCreator/")

# Program

m.title()
while True:
    o = m.mainMenu()
    if o == "": pass
    elif o == "c":
        m.create()
    elif o == "o":
        o = m.selector()
        if not o: pass
        else:
            h = Hierarchy(o, f"{o}")
            m.creator(h)
    elif o == "t":
        m.tutorial()
    elif o == "i":
        m.info()
    elif o == "e":
        cls()
        break
    else:
        cls()
        print(m.error(f"Option \"{o}\" not found."))
        key()
