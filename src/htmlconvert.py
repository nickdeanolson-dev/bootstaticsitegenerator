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
            processed_blocks.append((blocktype, f"<p>{block}</p>"))
        elif blocktype == BlockType.HEADING:
            heading_level = block.count("#", 0, block.find(" "))
            heading = f"<h{heading_level}>{block[heading_level + 1:].strip()}</h{heading_level}>"
            processed_blocks.append((blocktype, heading))
        elif blocktype == BlockType.CODE:
            processed_blocks.append((blocktype, block[4:-3]))
        elif blocktype == BlockType.QUOTE:
            quote_content = "\n".join(line[1:].strip() for line in block.split("\n"))
            processed_blocks.append((blocktype, f"<blockquote>{quote_content}</blockquote>"))
        elif blocktype == BlockType.UNORDERED_LIST:
            list_items = [line[2:].strip() for line in block.split("\n")]
            list_html = "".join(f"<li>{item}</li>" for item in list_items)
            processed_blocks.append((blocktype, f"<ul>{list_html}</ul>"))
        elif blocktype == BlockType.ORDERED_LIST:
            list_items = [line.split(". ", 1)[1].strip() for line in block.split("\n")]
            list_html = "".join(f"<li>{item}</li>" for item in list_items)
            processed_blocks.append((blocktype, f"<ol>{list_html}</ol>"))

    html_nodes = []
    for blocktype, content in processed_blocks:
        if blocktype == BlockType.CODE:
            code_node = LeafNode(None, content)
            html_nodes.append(ParentNode("pre", [ParentNode("code", [code_node])]))
            continue
        for text_node in text_to_textnodes(content):
            html_nodes.append(text_node_to_html_node(text_node))

    return ParentNode("div", html_nodes)


