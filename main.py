from cefpython3 import cefpython as cef
import sys, os
import frontend.bindings as bindings
import gui.generator as generator

cef.Initialize() ## Initialize cefpython

## Display start page
window = cef.CreateBrowserSync(url=cef.GetDataUrl(generator.generate(page="start")), window_title="chunkl")

bindings.bind(browser=window) ## Bind python functions to javascript

cef.MessageLoop() ## Initialize cefpython main loop

## Clean up
del window
cef.Shutdown()
