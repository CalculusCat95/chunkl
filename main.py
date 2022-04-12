from cefpython3 import cefpython as cef
import sys, os
from gui.page import *

cef.Initialize() ## Initialize cefpython

## Display start page
page("start")

cef.MessageLoop() ## Initialize cefpython main loop

cef.Shutdown() ## Clean up
