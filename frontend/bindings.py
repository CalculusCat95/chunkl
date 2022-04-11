from cefpython3 import cefpython as cef
import backend.backend as backend

def bind(browser):
    
    bindings = cef.JavascriptBindings() ## Initializes cefpython JavascriptBindings class

    ## Binds functions to javascript
    bindings.SetFunction("build", backend.build)

    browser.SetJavascriptBindings(bindings) ## Passes bindings to cefpython