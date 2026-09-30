from textnode import TextNode, TextType

def main():
    trial = TextNode("This is some anchor text", TextType.BOLD, "https://boot.dev")
    print(trial)

main()