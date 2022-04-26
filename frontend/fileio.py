"""This file contains the functions fileRead and fileWrite. They are exposed to javascript."""
import tkinter as tk
from tkinter import filedialog
from initialize_cef import *

projectfile = None ## Creates projectfile variable to be sent to javascript pages
projectpath = None ## Creates projectpath variable to record file path
##Function to read files
def fileRead():

    global projectfile ## Brings in project file to be updated
    global projectpath ## Brings in project path
    ## Gets file path to open with tkinter
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename(title="Open a chunkl project")
    projectpath = path
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
def fileWrite(content):
    global projectpath
    ## Open the file and write the content to it
    f = open(projectpath, "w")
    f.write(str(content))
    f.close()

def getSavePath():
    global projectpath
    root = tk.Tk()
    root.withdraw()
    path = filedialog.path = filedialog.asksaveasfilename(title="Save a chunkl project", defaultextension=".chunkl", filetypes=[("Chunkl Project", "*.chunkl")])
    projectpath = path

def sendToJs (): ## Can be called from javascript to send the project to the gui

    window.ExecuteFunction("loadProject", projectfile) ## Send the page the project

def updateProjectFile (file): ## Updates the version of the file stored in python
    global projectfile
    projectfile = file
