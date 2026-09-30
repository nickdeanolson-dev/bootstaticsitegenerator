class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError("to_html method must be implemented in subclasses")
    def props_to_html(self):
        if not self.props or self.props == {}:
            return ""
        props_str = " ".join(f'{key}: "{value}",' for key, value in self.props.items())
        return f" {props_str}"
    def __repr__(self):
        print(f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})")


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None):
        super().__init__(tag, value, None, props)
    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode value cannot be None")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    def __repr__(self):
        print(f"HTMLNode(tag={self.tag}, value={self.value}, props={self.props})")


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict = None):
        super().__init__(tag = tag, value = None, children = children, props = props)
    def to_html(self):
        if self.children == None:
            raise ValueError("ParentNode children cannot be None")
        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def props_to_html(self):
        if not self.props or self.props == {}:
            return ""
        props_str = " ".join(f'{key}: "{value}",' for key, value in self.props.items())
        return f" {props_str}"
    def __repr__(self):
        print(f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})")