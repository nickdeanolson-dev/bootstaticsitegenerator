from textnode import TextNode, TextType
import os
import shutil


def main():
    trial = TextNode("This is some anchor text", TextType.BOLD, "https://boot.dev")
    print(trial)

main()