# Hierarchy Creator by dacoder101
# func.py

# Imports

from os import listdir as lsDir
from os import mkdir as mkDir
from os import remove as rmFile
from os import system as sys
import os

from console.utils import wait_key as key
from console import fx

from shutil import rmtree as rmDir

# Setup

unallowed = r'\/:*"<>| '
kpress = f"{fx.italic}Press Any Key...{fx.end}"
error = f"{fx.italic + fx.bold}Error:"
arrow = f"{fx.bold}>>{fx.end} "
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

    def success(str):
        return f"{Menu.boldText('Sucess!')} {str}\n{kpress}\n"

    def error(str):
        return f"{error}{fx.end} {str}\n{kpress}\n"

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
                f"{Menu.boldText('Select an Option')}\n\n[C]: Create New Hierarchy\n[O]: Open an Existing Hierarchy\n[T]: Tutorial for Creator\n[I]: Information\n[E]: Exit Hierarchy Editor\n\n{arrow}"
            ).lower().strip()
        except:
            Menu.mainMenu()

    def tutorial():
        cls()
        print(
            f"{Menu.boldText(f'Tutorial:')}\n\nUsing the Creator is like using a basic terminal.\nRemember that the hierarchy and directory are always shown at the top of the screen.\nTo create a file or directory, use create [file/dirname (end in /)].\nTo read a file, type cat [filename].\nWant to write to a file? Use write [filename] to begin the writing process.\nDeleting a file is as simple as using del [file/dirname (needs to end in /)].\nChange directory? Use cd [dirname]. cd also allows you to change back to the previous directory (../).\nWant to list files of a directory without entering? Use dir or ls, each works!\nDone with your file writing or want to leave the hierarchy? Simply type exit.\n\nThis terminal is guided to shift less technical users into using some basic terminal commands.\n{kpress}"
        )
        key()

    def info():
        cls()
        print(
            f"{Menu.boldText(f'Hierarchy Creator{newline}By dacoder101')}\n{Menu.italicText('Made for Pyos3')}\n\nHierarchy Creator allows your to create custom hierarchies with possibly needed information on pyos.\nMore information can be found at https://github.com/dacoder101/HierarchyCreator/\n\n{kpress}"
        )
        key()

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

    def selector():
        dirs = lsDir("HierarchyCreator/")
        while True:
            cls()
            for dir in dirs:
                if not os.path.isdir(f"HierarchyCreator/{dir}"):
                    dirs.remove(dir)
            dirs = sorted(dirs)
            printStr = f"{Menu.boldText(f'Type {quotation}exit{quotation} to exit.{newline}Type {quotation}del [hierarchy]{quotation} to delete.{newline + newline}Available Hierarchies')}\n\n"
            if dirs != []:
                for f in dirs:
                    printStr += f" ↳ \"{f}\"\n"
                printStr += f"\n{arrow}"
            else:
                print(
                    Menu.error(
                        "No valid hierarchies found.\nCreate a new one."))
                key()
                break
            try:
                o = input(printStr).strip()
                cls()
                h = Hierarchy(o, o)
                if h.check(): return o
                else:
                    r = Command.selector(o.split())
                    if r == None: pass
                    elif r != False:
                        if r == "exit": break
                        print(r)
                        key()
                    else:
                        print(
                            Menu.error(
                                f"No command or hierarchy was found. \"{o}\"\nCapitalization is nessesary."
                            ))
                        key()
            except:
                pass

    def creator(obj):
        while True:
            cls()
            currentDir = obj.getDir()
            currentDir = currentDir.replace("//", "/")
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
                    "No files or directories were found.\nFind information on creating files and directories in the Tutorial.\nType \"exit\" to exit to the creator.\n"
                )
            try:
                o = input(f"{printStr}{newline}{arrow}").strip()
                cls()
                if o == "": pass
                else:
                    o = o.strip()
                    r = Command.command(o.split(), obj)
                    if r == "exit": break
                    elif r == None: pass
                    elif r != False:
                        print(r)
                        key()
                    else:
                        print(
                            Menu.error(f"The command \"{o}\" does not exist."))
                        key()
            except:
                pass


# Command


class Command:

    def selector(c):
        main = c[0].lower()
        try:
            arg = c[1]
        except:
            pass
        try:
            print(
                f"{Menu.boldText('Info:')} \"{c[2]}\" and any other queries were ignored as they will not be used.\n{kpress}"
            )
            key()
        except:
            pass
        if main == "exit": return "exit"
        elif main == "del":
            try:
                if arg == "*":
                    try:
                        o = input(
                            f"{Menu.boldText('Warning: ')} This operating will delete EVERYTHING in EVERY hierarchy.\nType \"OK\" to confirm.\n\n{arrow}"
                        ).lower().strip()
                        if o == "ok":
                            cls()
                            for f in lsDir("HierarchyCreator"):
                                if os.path.isdir(f"HierarchyCreator/{f}"):
                                    rmDir(f"HierarchyCreator/{f}")
                                else:
                                    rmFile(f"HierarchyCreator/{f}")
                            cls()
                            return Menu.success(
                                "All hierarchies and their contents were deleted."
                            )
                    except:
                        pass
                elif os.path.isdir(f"HierarchyCreator/{arg}"):
                    rmDir(f"HierarchyCreator/{arg}")
                    return Menu.success(f"Deleted hierarchy \"{arg}\".")
                else:
                    return Menu.error(f"Unable to locate hierarchy \"{arg}\"")
            except:
                return Menu.error(
                    "An issue occured while processing your del command.")
        else:
            return False

    def command(c, obj):
        main = c[0].lower()
        try:
            arg = c[1]
        except:
            pass
        legalDir = obj.getLegalDir()
        try:
            print(
                f"{Menu.boldText('Info:')} \"{c[2]}\" and any other queries were ignored as they will not be used.\n{kpress}"
            )
            key()
        except:
            pass
        cls()
        if main == "exit": return "exit"
        elif main == "create":
            try:
                if arg[-1] == "/":
                    mkDir(f"{legalDir}/{arg}")
                    return Menu.success(
                        f"Created directory \"{arg.replace('/', '')}/\".")
                else:
                    Function.openX(f"{legalDir}/{arg}")
                    return Menu.success(f"Created file \"{arg}\".")
            except:
                return Menu.error(
                    "An issue occured while proccessing your create command.\nDue to limitations a directory and file cannot have the same name."
                )
        elif main == "del":
            try:
                if lsDir(legalDir) == []:
                    return Menu.error("No files to delete were found.")
                elif arg == "*":
                    try:
                        o = input(
                            f"{Menu.boldText('Warning: ')} This operating will delete ALL files and folders within this directory.\nType \"OK\" to confirm.\n\n{arrow}"
                        ).lower().strip()
                        if o == "ok":
                            cls()
                            for f in lsDir(legalDir):
                                if os.path.isdir(f"{legalDir}/{f}"):
                                    rmDir(f"{legalDir}/{f}")
                                else:
                                    rmFile(f"{legalDir}/{f}")
                            return Menu.success(
                                "All files and directories were deleted.")

                    except:
                        pass
                elif arg[-1] == "/":
                    rmDir(f"{legalDir}/{arg}")
                    return Menu.success(f"Deleted directory \"{arg}\".")
                else:
                    rmFile(f"{legalDir}/{arg}")
                    return Menu.success(f"Deleted file \"{arg}\".")
            except:
                return Menu.error(
                    "An issue occured while processing your del command.\nNote that deleteing a directory requires a backslash. (Ex: \"del ex/\")"
                )
        elif main == "cd":
            if arg == "/":
                obj.changeDir(obj.__str__())
            elif arg == "../" or arg == "/..":
                if obj.getDir() == f"{obj}/":
                    return Menu.error("You cannot cd any further back.")
                else:
                    backDir = obj.getDir().split("/")
                    backDir = [v for v in backDir if v != ""]
                    backDir.pop()
                    backDirStr = ""
                    for d in backDir:
                        backDirStr += d + "/"
                    obj.changeDir(backDirStr)
            elif arg == "./" or arg == "/.":
                pass
            elif os.path.exists(f"{legalDir}/{arg}") and os.path.isdir(
                    f"{legalDir}/{arg}") and arg[0] != "/" and arg != ".":
                dir = f"{obj.getDir()}/{arg}"
                obj.changeDir(dir)
            else:
                return Menu.error(
                    "An issue occured while processing your cd command.\nNote that you cannot cd into a file."
                )
        elif main == "cat":
            try:
                if arg in lsDir(legalDir):
                    if len(Function.openR(f"{legalDir}/{arg}")) < 1:
                        printStr = f"{Menu.boldText(f'Reading File: /{obj.getDir()}/{arg}/'.replace('//', '/'))}\n\n{Menu.italicText(f'This file is empty.{newline}You can write to it using {quotation}write [{arg}]{quotation}')}\n\n{kpress}"
                    else:
                        printStr = f"{Menu.boldText(f'Reading File: /{obj.getDir()}/{arg}/'.replace('//', '/'))}\n\n{Function.openR(f'{legalDir}/{arg}')}\n\n{kpress}"
                    print(printStr)
                    key()
            except:
                return Menu.error(
                    "An issue occured while processing your cat command.\nNote you cannot cat a folder."
                )
        else:
            return False


# Function


class Function:

    def openR(file):
        with open(file, "r") as file:
            return file.read().strip()

    def openW(file, w):
        with open(file, "w") as file:
            file.write(w)

    def openX(file):
        f = open(file, "x")
        f.close()


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
                        f"The name of \"{name}\" includes one or more of the following: {unallowed}and whitespace."
                    ))
                key()
                return False
        if name.lower() == "exit" or name.lower() == "del":
            print(
                Menu.error(
                    "Your hierarchy cannot be named \"exit\" or \"del\"."))
            key()
            return False
        if name in lsDir("HierarchyCreator/"):
            print(Menu.error(f"The name of \"{name}\" is already in use."))
            key()
            return False
        mkDir(f"HierarchyCreator/{name}/")
        print(
            f"{fx.bold}Success!{fx.end} New hierarchy \"{name}\" created.\n{kpress}"
        )
        key()
        return True

    def check(self):
        if self.dir[:-1] in lsDir("HierarchyCreator/"): return True
        return False

    def changeDir(self, dir):
        if dir[-1] != "/":
            self.dir = dir + "/"
        else:
            self.dir = dir

    def getDir(self):
        return self.dir

    def getLegalDir(self):
        return f"HierarchyCreator/{self.dir}"
