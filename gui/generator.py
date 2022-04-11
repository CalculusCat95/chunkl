""" 
This class contains the 'generator' function. This function generates an html page containing all the necessary
html, css, and javascript for the GUI. The page is then returned as a string.

"""

## (delete this after u read it) I did some research and it seems that in this case, it's better to have a function than a 
## class. it seems like you use a class to do something TO the data and a function to do something WITH the data 
##(or make the data)

def generate (page):
    
    ## Opens the three files for the given page
    htmlfile = open("gui/" + page + ".html","r")
    jsfile = open("gui/" + page + ".js","r")
    cssfile = open("gui/" + page + ".css","r")
    
    ## Reads the contents of the files
    html = htmlfile.read()
    js = jsfile.read()
    css = cssfile.read()

    html = html.format(javascript=js, style=css) ## Formats all the code into one large string
    
    ## Closes the files
    htmlfile.close()
    jsfile.close()
    cssfile.close()

    ## Outputs the combined result
    return html