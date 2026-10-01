from textnode import TextNode, TextType

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


