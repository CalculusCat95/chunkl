class Page:
    def __init__ (self, page):
        self.page = page

    def generate (page):
        htmlfile = open("gui/" + page + ".html","r")
        jsfile = open("gui/" + page + ".js","r")
        cssfile = open("gui/" + page + ".css","r")
        html = htmlfile.read()
        js = jsfile.read()
        css = cssfile.read()
        html = html.format(javascript=js, style=css)
        print(jsfile.read())
        htmlfile.close()
        jsfile.close()
        cssfile.close()
        return html

"""This file should take the page to load as an argument of some sort. Then, it should take the necessary html, css, and js
files, place them in the necessary tags in an html skeleton in a string, and return them to the main.py file to be displayed."""