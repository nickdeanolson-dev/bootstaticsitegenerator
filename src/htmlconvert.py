from html import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from markup import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from blockmarkup import BlockType, markdown_to_blocks, block_to_block_type

def markdown_to_html_node(markdown):
    #print("Markdown to HTML Node:\n", markdown)  # Debugging print statement
    blocks = markdown_to_blocks(markdown)
    processed_blocks = []
    for block in blocks:
        blocktype = block_to_block_type(block)
        if blocktype == BlockType.PARAGRAPH:
            text_nodes = text_to_textnodes(block)
            html_nodes = []
            for node in text_nodes:
                html_nodes.append(text_node_to_html_node(node))
            processed_blocks.append(ParentNode("p", html_nodes))
        elif blocktype == BlockType.CODE:
            processed_blocks.append(ParentNode("pre", [ParentNode("code", [LeafNode(None, block[4:-3])])]))
        elif blocktype == BlockType.HEADING:
            html_nodes = []
            heading_level = block.count("#", 0, block.find(" "))
            text_nodes = text_to_textnodes(block[heading_level+1:].strip())
            for node in text_nodes:
                html_nodes.append(text_node_to_html_node(node))
            processed_blocks.append(ParentNode(f"h{heading_level}", html_nodes))
        elif blocktype == BlockType.QUOTE:
            qlist = block.split("\n")
            plist = []
            for l in qlist:
                plist.append(l[1:].strip())
            block = " ".join(plist)
            text_nodes = text_to_textnodes(block)
            html_nodes = []
            for node in text_nodes:
                html_nodes.append(text_node_to_html_node(node))
            processed_blocks.append(ParentNode("blockquote", html_nodes))
        elif blocktype == BlockType.UNORDERED_LIST:
            list_items = [line[2:].strip() for line in block.split("\n")]
            processed_list_items = []
            for li in list_items:
                html_nodes = []
                text_nodes = text_to_textnodes(li)
                for node in text_nodes:
                    html_nodes.append(text_node_to_html_node(node))
                processed_list_items.append(ParentNode("li",html_nodes))
            processed_blocks.append(ParentNode("ul", processed_list_items))
        elif blocktype == BlockType.ORDERED_LIST:
            list_items = [line.split(". ", 1)[1].strip() for line in block.split("\n")]
            processed_list_items = []
            for li in list_items:
                html_nodes = []
                text_nodes = text_to_textnodes(li)
                for node in text_nodes:
                    html_nodes.append(text_node_to_html_node(node))
                processed_list_items.append(ParentNode("li",html_nodes))
            processed_blocks.append(ParentNode("ol", processed_list_items))

    return ParentNode("div", processed_blocks)


