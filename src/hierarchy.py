# Hierarchy Creator by dacoder101
# hierarchy.py

# Imports

from func import Menu as m
from func import Command as c
from func import Function as f
from func import Hierarchy

from os import listdir as lsDir
from os import mkdir as mkDir
from os import remove as rmFile
from os import system as sys
import os

from console.utils import wait_key as key
from console import fx

from shutil import rmtree as rmDir

# Setup


def cls():
    sys('clear')


if "HierarchyCreator" not in lsDir():
    mkDir("HierarchyCreator/")

# Program


def main():
    m.title()
    while True:
        o = m.mainMenu()
        if o == "": pass
        elif o == "c":
            m.create()
        elif o == "o":
            o = m.selector()
            if not o or o == None: pass
            else:
                h = Hierarchy(o, o)
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
            if o != None:
                print(m.error(f"The option \"{o}\" has not been found."))
                key()


if __name__ == "__main__": main()
