from cefpython3 import cefpython as cef
import sys, os

def printstuff(text):
    print(text)
    
sys.excepthook = cef.ExceptHook
settings = {"debug": False, "log_file": ""}
cef.Initialize(settings=settings)
cef.CreateBrowserSync(url="file:///./main.html", window_title="chunkl")
cef.JavascriptBindings(bindToFrames=True, bindToPopups=True).SetFunction("alert", printstuff)

cef.MessageLoop()

cef.Shutdown()
