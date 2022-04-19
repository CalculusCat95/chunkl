"""This file contains the functions fileRead and fileWrite. They are exposed to javascript."""
import tkinter as tk
from tkinter import filedialog
from initialize_cef import *
from cefpython3 import cefpython as cef

##Function to read files
def fileRead():

    root = tk.Tk()
    root.withdraw()

    path = filedialog.askopenfilename()

    try:
        f = open(path, "r")

        r = f.read()

        f.close()
        
        js = """function{{console.log({file});}};"""

        cookie = cef.Cookie()
        cookie.Set({"name": "project", "value": r})

        window.ExecuteFunction("loadProject", r)

    except:
        pass

##Function to write values to files
def fileWrite(path, content):

    f = open(path, "w")

    f.write(str(content))

    f.close()

## For debug purposes 
def printToPython(str):

    print(str)