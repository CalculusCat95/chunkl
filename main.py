from cefpython3 import cefpython as cef
import sys, os

cef.Initialize() ## Initialize cefpython

from gui.page import * ## Start the gui rolling

cef.MessageLoop() ## Initialize cefpython main loop
cef.Shutdown() ## Clean up
