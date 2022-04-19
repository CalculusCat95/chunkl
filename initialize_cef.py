from cefpython3 import cefpython as cef
import sys

cef.Initialize() ## Initialize cefpython

sys.excepthook = cef.ExceptHook ## Allow cefpython to handle Python errors so that stuff can be cleaned up

window = cef.CreateBrowserSync(window_title="chunkl") ## Display start page