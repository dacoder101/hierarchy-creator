# Hierarchy Creator by dacoder101
# func.py

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

kpress = f"{fx.italic}Press Any Key...{fx.end}"
hierarchy = ""


def cls():
    sys('clear')


if "HierarchyCreator" not in lsDir():
    mkDir("HierarchyCreator")

# Program

m.title()
while True:
    o = m.mainMenu()

    if o == "": pass
    elif o == "c":
        m.create()
    elif o == "o":
        option = m.selector()
        if not option: pass
        else:
            h = Hierarchy(option)
            cls()
            print(f"WIP!\n{kpress}")
            key()
    elif o == "i":
        m.info()
    elif o == "e":
        cls()
        break
    else:
        cls()
        print(
            f"{fx.italic}Error: Option \"{o}\" was not found.\nPress Any Key...{fx.end}"
        )
        key()
