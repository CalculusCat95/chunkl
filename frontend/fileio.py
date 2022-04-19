"""This file contains the functions fileRead and fileWrite. They are exposed to javascript."""
import tkinter as tk
from tkinter import filedialog
from initialize_cef import *
from cefpython3 import cefpython as cef

projectfile = None ## Creates projectfile variable to be sent to javascript pages

##Function to read files
def fileRead():

    global projectfile ## Brings in project file to be updated
    ## Gets file path to open with tkinter
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename()

    try: ## Ensures that it doesn't do anything if they close the file dialog
        ## Opens the file and reads it into a variable
        f = open(path, "r")
        r = f.read()
        f.close()
        
        projectfile = r ## Updates the projectfile variable to be sent to javascript

        window.ExecuteFunction("loadProject", projectfile)

    except:
        pass

##Function to write values to files
def fileWrite(path, content):

    f = open(path, "w")

    f.write(str(content))

    f.close()

def sendToJs ():

    window.ExecuteFunction("loadProject", projectfile) ## Send the page the project

def updateProjectFile (file):
    global projectfile
    projectfile = file
