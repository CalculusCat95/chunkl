"""This file contains the functions fileRead and fileWrite. They are exposed to javascript."""
import tkinter as tk
from tkinter import filedialog
from initialize_cef import *

##Function to read files
def fileRead():

    root = tk.Tk()
    root.withdraw()

    path = filedialog.askopenfilename()

    print(path)

    f = open(path, "r")

    r = f.read()

    f.close()

    print(r)
    
    js = """function{{console.log({file});}};"""

    window.ExecuteFunction("loadProject", r)

##Function to write values to files
def fileWrite(path, content):

    f = open(path, "w")

    f.write(str(content))

    f.close()

## For debug purposes 
def printToPython(str):

    print(str)