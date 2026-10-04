from textnode import TextNode, TextType
import os
import shutil

def reset(source_path, dest_path):
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
            copier(source_path=next_source,dest_path=next_dest)
        else:
            shutil.copy(next_source, next_dest)
        



def main():
    reset("./static", "./public")

main()