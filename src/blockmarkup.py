
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def markdown_to_blocks(markdown):
    # Split the markdown into blocks based on double newlines
    blocks = markdown.split("\n\n")
    result_blocks = []
    for b in blocks:
        if b.strip() != "\n":
            b = b.strip()
            result_blocks.append(b)

    return result_blocks

def block_to_block_type(block) -> BlockType:
    # Determine the type of block based on its content
    if block[:1] == ">":
        lines = block.split("\n")
        for l in lines:
            if l[:1] != ">":
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    elif block[:2] == "# " or block[:3] == "## " or block[:4] == "### " or block[:5] == "#### " or block[:6] == "##### " or block[:7] == "###### ":
        return BlockType.HEADING
    elif block[:4] == "```\n" and block[-3:] == "```":
        return BlockType.CODE
    elif block[:2] == "- ":
        lines = block.split("\n")
        for l in lines:
            if l[:2] != "- ":
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    elif block[:3] == "1. ":
        row = 1
        lines = block.split("\n")
        for l in lines:
            if l.split(". ", 1)[0] != f"{row}":
                return BlockType.PARAGRAPH
            row += 1
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

    