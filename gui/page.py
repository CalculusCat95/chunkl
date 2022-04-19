""" 
This class contains the 'page' function. This function generates an html page containing all the necessary
html, css, and javascript for the GUI and renders it in a cefpython window.

"""
from cefpython3 import cefpython as cef
import frontend.bindings as bindings
from initialize_cef import *
import time

def generate (page):
    
    ## Opens the three files for the given page
    htmlfile = open("gui/" + page + '/' + page + ".html","r")
    jsfile = open("gui/" + page + '/' + page + ".js","r")
    cssfile = open("gui/" + page + '/' + page + ".css","r")
    
    ## Reads the contents of the files
    html = htmlfile.read()
    js = jsfile.read()
    css = cssfile.read()

    html = html.format(javascript=js, style=css) ## Formats all the code into one large string
    
    ## Closes the files
    htmlfile.close()
    jsfile.close()
    cssfile.close()

    return html ## Return result

def page (page, project):

    window.LoadUrl(cef.GetDataUrl(generate(page))) ## Generates the correct page and displays it
    time.sleep(0.05)
    window.ExecuteFunction("loadProject", project) ## Send the page the project

bindings.bind(page=page) ## Bind Python functions to Javascript