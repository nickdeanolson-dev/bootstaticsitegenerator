from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    return_nodes = []
    for node in old_nodes:
        new_nodes = []
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            old_type = node.text_type
            parts = node.text.split(delimiter)
            if len(parts)%2 == 0:
                raise ValueError(f"Unmatched delimiter '{delimiter}' in text: {node.text}")
            apply = False
            for p in parts:
                if apply:
                    new_nodes.append(TextNode(p, text_type))
                    apply = False
                else:
                    new_nodes.append(TextNode(p, old_type))
                    apply = True
        return_nodes.extend(new_nodes)
    return return_nodes


def extract_markdown_images(text: str):
    return re.findall(r'!\[(.*?)\]\((.*?)\)', text)


def extract_markdown_links(text: str):
    return re.findall(r'(?<!\!)\[(.*?)\]\((.*?)\)', text)


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    returnlist = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        linetext = ""
        linetext = node.text
        if len(images) > 0:
            for i in images:
                istring = (f"![{i[0]}]({i[1]})")
                splittext = linetext.split(istring)
                if splittext[0] != "":
                    returnlist.append(TextNode(splittext[0], TextType.TEXT))
                returnlist.append(TextNode(i[0], TextType.IMAGE, i[1]))
                linetext = splittext[1]
            if linetext != "":
                returnlist.append(TextNode(linetext, TextType.TEXT))
        else:
            returnlist.append(node)
    return returnlist




def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    returnlist = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        linetext = ""
        linetext = node.text
        if len(links) > 0:
            for l in links:
                lstring = (f"[{l[0]}]({l[1]})")
                splittext = linetext.split(lstring)
                if splittext[0] != "":
                    returnlist.append(TextNode(splittext[0], TextType.TEXT))
                returnlist.append(TextNode(l[0], TextType.LINK, l[1]))
                linetext = splittext[1]
            if linetext != "":
                returnlist.append(TextNode(linetext, TextType.TEXT))
        else:
            returnlist.append(node)
    return returnlist


def text_to_textnodes(text):
    resultlist = []
    resultlist = [TextNode(text, TextType.TEXT)]
    resultlist = split_nodes_delimiter(resultlist, "**", TextType.BOLD)
    resultlist = split_nodes_delimiter(resultlist, "_", TextType.ITALIC)
    resultlist = split_nodes_delimiter(resultlist, "`", TextType.CODE)
    resultlist = split_nodes_image(resultlist)
    resultlist = split_nodes_link(resultlist)
    return resultlist


def markdown_to_blocks(markdown):
    # Split the markdown into blocks based on double newlines
    blocks = markdown.split("\n\n")
    result_blocks = []
    for b in blocks:
        if b.strip() != "\n":
            b = b.strip()
            result_blocks.append(b)

    return result_blocks