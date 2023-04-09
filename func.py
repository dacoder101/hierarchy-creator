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
kpress = f"{fx.italic}Press Any Key...{fx.end}"
error = f"{fx.italic + fx.bold}Error: "
newline = "\n"
quotation = "\""


def cls():
    sys('clear')


# Menu


class Menu:

    def error(str):
        return f"{error}{str}{fx.end}\n{kpress}\n"

    def boldtext(str):
        return f"{fx.bold}{str}{fx.end}"

    def italictext(str):
        return f"{fx.italic}{str}{fx.end}"

    def arrow():
        return f"{fx.bold}>>{fx.end} "

    def title():
        cls()
        print(
            f"{Menu.boldtext(f'Hierarchy Creator{newline}dacoder101')}\n\n{kpress}"
        )
        key()

    def mainMenu():
        cls()
        try:
            return input(
                f"{Menu.boldtext('Select an Option')}\n\n[C]: Create New Hierarchy\n[O]: Open an Existing Hierarchy\n[I]: Information\n[E]: Exit Hierarchy Editor\n\n{Menu.arrow()}"
            ).lower().strip()
        except:
            Menu.mainMenu()

    def create():
        while True:
            cls()
            try:
                name = input(
                    f"{Menu.boldtext('Create Hierarchy')}\n\nName: ").strip()
            except:
                Menu.create()
            cls()
            h = Hierarchy(name)
            if h.create(): break

    def info():
        cls()
        print(
            f"{Menu.boldtext(f'Hierarchy Creator{newline}By dacoder101')}\n{Menu.italictext('Made for Pyos3')}\n\nHierarchy Creator allows your to create custom hierarchies with possibly needed information on pyos.\n\n{kpress}"
        )
        key()

    def selector():
        cls()
        dirs = lsDir("HierarchyCreator")
        for dir in dirs:
            if "." in dir: dirs.remove(dir)
        dirs = sorted(dirs)

        printStr = f"{Menu.boldtext('Available Hierarchies')}\n\n"
        if dirs != []:
            for f in dirs:
                printStr += f" ↳ \"{f}\"\n"
            printStr += f"\n{Menu.arrow()}"
        else:
            print(Menu.error("No valid hierarchies found."))
            key()
            return False
        while True:
            cls()
            try:
                o = input(printStr).strip()
                h = Hierarchy(o)
                if h.check(): break
                else:
                    if o == "": pass
                    else:
                        cls()
                        print(
                            Menu.error(
                                f"Hierarchy \"{o}\" was not found.\nCorrect captialization and spacing is nessesary."
                            ))
                        key()
            except:
                pass
        return o

    def creator(object):
        while True:
            cls()
            files = []
            dir = Menu.boldtext(f"Directory: {quotation}/{object}/{quotation}")
            printStr = f"{Menu.boldtext(f'Hierarchy: {quotation}{object}{quotation}')}\n{dir}\n\n"
            for file in lsDir(f"HierarchyCreator/{object}/"):
                files.append(file)
            if files != []:
                for file in files:
                    printStr += f" ↳ \"{file}\"\n"
            else:
                printStr += Menu.italictext(
                    "No files or directories were found.\nCreate a new one.\n\n")
            printStr = f"{printStr}\n{Menu.arrow()}"
            o = input(printStr)


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

    def __str__(self):
        return self.name

    def create(self):
        name = self.name
        for char in name:
            if char in unallowed:
                print(
                    Menu.error(
                        f"The name \"{name}\"includes unallowed characters."))
                key()
                return False
        if name in lsDir("HierarchyCreator"):
            print(Menu.error(f"The name \"{name}\"is already in use."))
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
