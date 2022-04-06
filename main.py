from cefpython3 import cefpython as cef
import sys, os

sys.excepthook = cef.ExceptHook
settings = {"debug": False, "log_file": ""}
cef.Initialize(settings=settings)
cef.CreateBrowserSync(url="file:///./main.html")

cef.MessageLoop()

cef.Shutdown()
