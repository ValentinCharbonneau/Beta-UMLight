import os
import sys

def list(path, content):
    for line in os.listdir(path):
        if os.path.isdir(os.path.join(path, line)):
            content = list(path + "/" + line, content)
        else:
            content += "\n" + path + "/" + line
    return content

f = open(sys.argv[2], "w")
f.write(list(sys.argv[1], "### files ###"))
f.close()

print("Done !")
