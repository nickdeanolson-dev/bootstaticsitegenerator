from enum import Enum


class TextType(Enum):
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type  
        self.url = url  # Only used for LINK and IMAGE types
    def __eq__(self, other: TextNode):
        if (self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url):
            return True
        return False
    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type}, {self.url})")