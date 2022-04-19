from cefpython3 import cefpython as cef
from gui.page import * ## Start the gui rolling

page("start")

cef.MessageLoop() ## Initialize cefpython main loop
cef.Shutdown() ## Clean up