from cefpython3 import cefpython as cef
import sys
import os
import backend.backend
from gen import *


cef.Initialize()
browser = cef.CreateBrowserSync(url=cef.GetDataUrl(Page.generate(page="start")), window_title="chunkl")
bindings = cef.JavascriptBindings()

bindings.SetFunction("build", backend.backend.build)
browser.SetJavascriptBindings(bindings)
cef.MessageLoop()
del browser
cef.Shutdown()
