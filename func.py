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

    def boldText(str):
        return f"{fx.bold}{str}{fx.end}"

    def italicText(str):
        return f"{fx.italic}{str}{fx.end}"

    def error(str):
        return f"{error}{str}{fx.end}\n{kpress}\n"

    def arrow():
        return f"{fx.bold}>>{fx.end} "

    def title():
        cls()
        print(
            f"{Menu.boldText(f'Hierarchy Creator{newline}dacoder101')}\n\n{kpress}"
        )
        key()

    def mainMenu():
        cls()
        try:
            return input(
                f"{Menu.boldText('Select an Option')}\n\n[C]: Create New Hierarchy\n[O]: Open an Existing Hierarchy\n[T]: Tutorial for Creator\n[I]: Information\n[E]: Exit Hierarchy Editor\n\n{Menu.arrow()}"
            ).lower().strip()
        except:
            Menu.mainMenu()

    def create():
        while True:
            cls()
            try:
                name = input(
                    f"{Menu.boldText('Create Hierarchy')}\n\nName: ").strip()
                cls()
                h = Hierarchy(name, name)
                if h.create(): break
            except:
                pass

    def info():
        cls()
        print(
            f"{Menu.boldText(f'Hierarchy Creator{newline}By dacoder101')}\n{Menu.italicText('Made for Pyos3')}\n\nHierarchy Creator allows your to create custom hierarchies with possibly needed information on pyos.\n\n{kpress}"
        )
        key()

    def tutorial():
        cls()
        print(
            f"{Menu.boldText(f'Tutorial:{newline + newline}')}Using the Creator is like using a basic terminal\nRemember that the hierarchy and directory are always shown at the top of the screen.\nTo create a file or directory, use cfile or cdir [file/dirname] of that file/dir.\nTo read a file, type cat [filename].\nWant to write to a file? Use write [filename] to begin the writing process.\nDeleting a file is as simple as using dfile or ddir [file/dirname].\nChange directory? Use cd [dirname]. cd also allows you to change back to the previous directory (../), or the root directory (/).\nWant to list files of a directory without entering? Use dir or ls, each works!\nDone with your file writing or want to leave the hierarchy? Simply type exit.\n\nThis terminal is guided to shift less technical users into using a terminal style.\n{kpress}"
        )
        key()

    def selector():
        dirs = lsDir("HierarchyCreator/")
        for dir in dirs:
            if not os.path.isdir(f"HierarchyCreator/{dir}"): dirs.remove(dir)
        dirs = sorted(dirs)
        printStr = f"{Menu.boldText('Available Hierarchies')}\n\n"
        if dirs != []:
            for f in dirs:
                printStr += f" ↳ \"{f}\"\n"
            printStr += f"\n{Menu.arrow()}"
        else:
            cls()
            print(Menu.error("No valid hierarchies found.\nCreate a new one."))
            key()
            return False
        while True:
            cls()
            try:
                o = input(printStr).strip()
                h = Hierarchy(o, o)
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

    def creator(obj):
        while True:
            cls()
            currentDir = obj.getDir()
            dirs = lsDir(obj.getLegalDir())
            folders = []
            files = []
            printStr = Menu.boldText(
                f"Hierarchy: \"{obj}\"\nDirectory: \"/{currentDir}\"\n\nAvailable Files:\n\n"
            )
            if dirs != []:
                for f in dirs:
                    if os.path.isdir(f"{obj.getLegalDir()}/{f}"):
                        folders.append(f + "/")
                    else:
                        files.append(f)
                folders = sorted(folders)
                files = sorted(files)
                dirs = folders + files
                for f in dirs:
                    printStr += f" ↳ \"{f}\"\n"
            else:
                printStr += Menu.italicText(
                    "No files or directories were found.\nFind information on creating files and directories in the Tutorial.\n"
                )
            try:
                o = input(f"{printStr}{newline}{Menu.arrow()}").strip()
                if o == "": pass
            except:
                pass


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

    def __init__(self, name, dir):
        self.name = name
        if dir[-1] != "/": dir += "/"
        self.dir = dir

    def __str__(self):
        return self.name

    def create(self):
        name = self.name
        for char in name:
            if char in unallowed:
                print(
                    Menu.error(
                        f"The name of \"{name}\"includes unallowed characters."
                    ))
                key()
                return False
        if name in lsDir("HierarchyCreator/"):
            print(Menu.error(f"The name of \"{name}\"is already in use."))
            key()
            return False
        mkDir(f"HierarchyCreator/{name}/")
        print(f"{fx.bold}Success!{fx.end} New hierarchy created.\n{kpress}")
        key()
        return True

    def check(self):
        if self.dir[:-1] in lsDir("HierarchyCreator/"): return True
        return False

    def changeDir(self, dir):
        if dir[-1] != "/": self.dir = dir + "/"
        else: self.dir = dir
        return dir

    def getDir(self):
        return self.dir

    def getLegalDir(self):
        return f"HierarchyCreator/{self.dir}"
