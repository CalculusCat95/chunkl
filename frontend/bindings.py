from cefpython3 import cefpython as cef
import backend.backend as backend
import frontend.fileio as fileio
from initialize_cef import *

def bind(page):
    
    bindings = cef.JavascriptBindings(bindToFrames=True) ## Initializes cefpython JavascriptBindings class

    ## Binds functions to javascript
    bindings.SetFunction("build", backend.build)
    bindings.SetFunction("fileRead", fileio.fileRead)
    bindings.SetFunction("fileWrite", fileio.fileWrite)
    bindings.SetFunction("page", page)
    bindings.SetFunction("print", fileio.printToPython)

    window.SetJavascriptBindings(bindings) ## Passes bindings to cefpython