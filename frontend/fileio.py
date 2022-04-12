"""This file contains the functions fileRead and fileWrite. They are exposed to javascript."""
##Function to read files
def fileRead(path):

    f = open(path, "r")

    r = f.read()

    f.close()
    
    return r

##Function to write values to files
def fileWrite(path, content):

    f = open(path, "w")

    f.write(str(content))

    f.close()