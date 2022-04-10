from cefpython3 import cefpython as cef
import sys
import os
import gui.gen
import backend.backend


cef.Initialize()
browser = cef.CreateBrowserSync(url=cef.GetDataUrl(gui.gen.html), window_title="chunkl")
bindings = cef.JavascriptBindings()

bindings.SetFunction("build", backend.backend.build)
browser.SetJavascriptBindings(bindings)

cef.MessageLoop()
del browser
cef.Shutdown()
