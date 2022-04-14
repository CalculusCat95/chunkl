from cefpython3 import cefpython as cef
import backend.backend as backend
import gui.page as page
import frontend.fileio as fileio

def bind(browser):
    
    bindings = cef.JavascriptBindings(bindToFrames=True) ## Initializes cefpython JavascriptBindings class

    ## Binds functions to javascript
    bindings.SetFunction("build", backend.build)
    bindings.SetFunction("fileRead", fileio.fileRead)
    bindings.SetFunction("fileWrite", fileio.fileWrite)
    bindings.SetFunction("page", page.page)
    bindings.SetFunction("print", fileio.printToPython)

    browser.SetJavascriptBindings(bindings) ## Passes bindings to cefpython