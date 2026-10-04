from textnode import TextNode, TextType
import os
import shutil

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
        



def main():
    copier("./static", "./public/")

main()