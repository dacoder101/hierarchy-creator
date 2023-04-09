# Imports

from func import Menu as m
from func import Function as f
from func import Hierarchy

from os import listdir as lsDir
from os import mkdir as mkDir
from os import system as sys

from console.utils import wait_key as key
from console import fx

# Setup

hierarchy = ""


def cls():
    sys('clear')


if "HierarchyCreator" not in lsDir():
    mkDir("./HierarchyCreator")

# Program

m.title()
while True:
    o = m.mainMenu()

    if o == "c": pass
    elif o == "o":
        rVal = m.selector()
        if not rVal: pass
        else: hierarchy = rVal
    elif o == "i":
        m.info()
    elif o == "e":
        cls()
        break
