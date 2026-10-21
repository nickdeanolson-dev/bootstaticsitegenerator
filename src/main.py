from textnode import TextNode, TextType
import os
import shutil
import sys
from htmlconvert import generate_page

def reset(source_path, dest_path):
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
    os.mkdir(dest_path)
    copier(source_path=source_path, dest_path=dest_path)

def copier(source_path, dest_path):

    items = os.listdir(source_path)
    for i in items:
        next_dest = os.path.join(dest_path, i)
        next_source = os.path.join(source_path, i)
        if not os.path.isfile(next_source):
            if not os.path.exists(next_dest):
                os.mkdir(next_dest)
            copier(source_path=next_source, dest_path=next_dest)
        else:
            shutil.copy(next_source, next_dest)

        
def content_gen(basepath, source_path, dest_path):
    items = os.listdir(source_path)
    for i in items:
        if not os.path.isfile(os.path.join(source_path, i)):
            if not os.path.exists(os.path.join(dest_path, i)):
                os.mkdir(os.path.join(dest_path, i))
            content_gen(basepath, source_path=os.path.join(source_path, i),dest_path=os.path.join(dest_path, i))
        else:
            if i[-3:] == ".md":
                shutil.copy(os.path.join(source_path, i), os.path.join(dest_path, i))
                generate_page(basepath, os.path.join(source_path, i), "template.html", os.path.join(dest_path, i[:-3]+".html"))


def main():
    basepath = sys.argv[1]
    print("basepath")
    print(basepath)
    reset("./static", "./docs")
    content_gen(basepath, "./content/", "./docs/")


main()