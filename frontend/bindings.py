from cefpython3 import cefpython as cef
import backend.backend as backend
from frontend.fileio import *
from initialize_cef import *

def bind(page):
    
    bindings = cef.JavascriptBindings(bindToFrames=True) ## Initializes cefpython JavascriptBindings class

    ## Binds functions to javascript
    bindings.SetFunction("build", backend.build)
    bindings.SetFunction("fileRead", fileRead)
    bindings.SetFunction("fileWrite", fileWrite)
    bindings.SetFunction("sendToJs", sendToJs)
    bindings.SetFunction("updateProjectFile", updateProjectFile)
    bindings.SetFunction("page", page)
    bindings.SetFunction("preview", backend.preview)
    bindings.SetFunction("getSavePath", getSavePath)

    window.SetJavascriptBindings(bindings) ## Passes bindings to cefpython