# Hierarchy Creator by dacoder101
# func.py

# Imports

from os import listdir as lsDir
from os import mkdir as mkDir
from os import system as sys
import os

from console.utils import wait_key as key
from console import fx

# Variables

unallowed = r'\/:*?"<>|'


def cls():
    sys('clear')


kpress = f"{fx.italic}Press Any Key...{fx.end}"

# Menu


class Menu:

    def title():
        cls()
        print(f"{fx.bold}Hierarchy Creator\ndacoder101{fx.end}\n\n{kpress}")
        key()

    def mainMenu():
        cls()
        try:
            return input(
                f"{fx.bold}Select an Option:{fx.end}\n\n[C]: Create New Hierarchy\n[O]: Open an Existing Hierarchy\n[I]: Information\n[E]: Exit Hierarchy Editor\n\n{fx.bold}>>{fx.end} "
            ).lower().strip()
        except:
            Menu.mainMenu()

    def create():
        while True:
            cls()
            try:
                name = input(
                    f"{fx.bold}Create Hierarchy:{fx.end}\n\nName: ").strip()
            except:
                Menu.create()
            cls()
            h = Hierarchy(name)
            if h.create(): break

    def info():
        cls()
        print(
            f"{fx.bold}Hierarchy Creator\nBy dacoder101\n{fx.italic}Made for Pyos3{fx.end}\n\nHierarchy Creator allows your to create custom hierarchies with possibly needed information on pyos.\n\n{kpress}"
        )
        key()

    def selector():
        cls()
        dirs = lsDir("HierarchyCreator")
        for dir in dirs:
            if "." in dir: dirs.remove(dir)
        dirs = sorted(dirs)

        printStr = f"{fx.bold}Available Hierarchies:{fx.end}\n\n"
        if dirs != []:
            for f in dir:
                printStr += f"↳ \"{f}\"\n"
            printStr += f"\n{fx.bold}>>{fx.end} "
        else:
            print(
                f"{fx.italic}Error: No valid hierarchies found.{fx.end}\n{kpress}"
            )
            key()
            return False
        while True:
            cls()
            try:
                option = input(printStr).strip()
                h = Hierarchy(option)
                if h.check(): break
                else:
                    cls()
                    print(
                        f"{fx.italic}Error: This hierarchy does not exist.\nCorrect captialization is nessesary.{fx.end}\n{kpress}"
                    )
                    key()
            except:
                pass
        return option


# Function


class Function:

    def openR(file):
        with open(file, "r") as file:
            return file.read()

    def openW(file, w=None):
        with open(file, "w") as file:
            try:
                file.write(w)
            except TypeError:
                pass


# Hierarchy


class Hierarchy:

    def __init__(self, name):
        self.name = name

    def create(self):
        name = self.name
        for char in name:
            if char in unallowed:
                print(
                    f"{fx.italic}Error: This name includes unallowed characters.{fx.end}\n{kpress}"
                )
                key()
                return False
        if name in lsDir("HierarchyCreator"):
            print(
                f"{fx.italic}Error: This name is already in use.{fx.end}\n{kpress}"
            )
            key()
            return False
        mkDir(f"HierarchyCreator/{name}")
        print(f"{fx.bold}Success!{fx.end} New hierarchy created.\n{kpress}")
        key()
        return True

    def check(self):
        name = self.name
        if name in lsDir("HierarchyCreator"): return True
        return False
