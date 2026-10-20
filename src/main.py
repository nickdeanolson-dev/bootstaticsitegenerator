from textnode import TextNode, TextType
import os
import shutil
from htmlconvert import generate_page

def reset(source_path, dest_path):
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
    os.mkdir(dest_path)
    copier(source_path=source_path, dest_path=dest_path)

def copier(source_path, dest_path):

    items = os.listdir(source_path)
    for i in items:
        if not os.path.isfile(source_path+"/"+i):
            if not os.path.exists(dest_path+i):
                os.mkdir(dest_path+i)
            copier(source_path=source_path+"/"+i,dest_path=dest_path+"/"+i)
        else:
            shutil.copy(source_path+"/"+i, dest_path+"/"+i)


        
def content_gen(source_path, dest_path):
    items = os.listdir(source_path)
    for i in items:
        if not os.path.isfile(os.path.join(source_path, i)):
            if not os.path.exists(os.path.join(dest_path, i)):
                os.mkdir(os.path.join(dest_path, i))
            content_gen(source_path=os.path.join(source_path, i),dest_path=os.path.join(dest_path, i))
        else:
            shutil.copy(os.path.join(source_path, i), os.path.join(dest_path, i))
            if i[-3:] == ".md":
                generate_page(os.path.join(source_path, i), "template.html", os.path.join(dest_path, i[:-3]+".html"))


def main():
    copier("./static", "./public/")
    #generate_page("content/index.md", "template.html", "public/index.html")
    content_gen("./content/", "./public/")


main()