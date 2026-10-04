from textnode import TextNode, TextType
import os
import shutil

def reset():
    shutil.rmtree("./public")

def copier(path):
    items = os.listdir(path)
    print(items)
    for i in items:
        print(os.path.isfile(path+"/"+i))
        if not os.path.isfile(path+"/"+i):
            print(i)
            copier(path+"/"+i)
    #print(os.listdir(folder))




def main():
    reset("./public")
    copier("./static")

main()