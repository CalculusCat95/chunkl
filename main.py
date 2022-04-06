from cefpython3 import cefpython as cef
import sys, os

sys.excepthook = cef.ExceptHook
cef.Initialize()
cef.CreateBrowserSync(url="file:///./main.html")
cef.MessageLoop()
cef.Shutdown()
