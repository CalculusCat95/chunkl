from cefpython3 import cefpython as cef
import sys, os

cef.Initialize() ## Initialize cefpython

sys.excepthook = cef.ExceptHook ## Allow cefpython to handle Python errors so that stuff can be cleaned up

from gui.page import * ## Start the gui rolling

cef.MessageLoop() ## Initialize cefpython main loop
cef.Shutdown() ## Clean up