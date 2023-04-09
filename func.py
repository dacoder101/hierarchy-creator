# Imports

from os import listdir as lsDir
from os import mkdir as mkDir
from os import system as sys

from console.utils import wait_key as key
from console import fx


def cls():
    sys('clear')


# Menu


class Menu:

    def title():
        cls()
        print("Hierarchy Creator\nBobbyPAC\n\nPress Any Key...")
        key()

    def mainMenu():
        cls()
        try:
            return input(
                "Select an Option:\n\n[C]: Create New Hierarchy\n[O]: Open an Existing Hierarchy\n[I]: Information\n[E]: Exit Hierarchy Editor\n\n>> "
            ).lower().strip()
        except:
            Menu.mainMenu()

    def create():
        cls()

    def info():
        cls()
        print(
            f"Hierarchy Creator\nBy BobbyPAC\n{fx.italic}Made for Pyos3{fx.end}\n\nHierarchy Creator allows your to create custom hierarchies with possibly needed information on pyos.\n\nPress Any Key..."
        )
        key()

    def selector():
        cls()
        dirs = lsDir("./HierarchyCreator")
        for dir in dirs:
            if "." in dir: dirs.remove(dir)
        dirs = sorted(dirs)

        printStr = "Available Hierarchies:\n\n"
        if dirs != []:
            for f in dir:
                printStr += f"↳ \"{f}\"\n"
        else:
            print(
                f"{fx.italic}Error: No valid hierarchies found.\nPress Any Key...{fx.end}"
            )
            key()
            return False
        return True


# Function


class Function:

    def f():

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

    def create():
        pass
