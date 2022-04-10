class Page:
    def __init__ (self, page):
        self.page = page
        self.html = html = """
        <!Doctype html>
        <html>
        <head></head>
        <body>
        <script>
        build(platform="windows", path="./projects/project.json");
        {javascript}
        </script>
        <style>
        {styles}
        </style>
        {html}
        </body>
        </html>
        """
    def generate (self, page):
        htmlfile = open(page + ".html","r")
        jsfile = open(page + ".js","r")
        cssfile = open(page + ".css","r")
        self.html.format(script = jsfile.read())
        htmlfile.close()
        jsfile.close()
        cssfile.close()
        return self.html

"""This file should take the page to load as an argument of some sort. Then, it should take the necessary html, css, and js
files, place them in the necessary tags in an html skeleton in a string, and return them to the main.py file to be displayed."""