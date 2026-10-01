import unittest
from html import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node

class TestHTMLNode(unittest.TestCase):
    def test_pth1(self):
        pass
    def test_pth2(self):
        node = HTMLNode("div", "This is aanother div", None, {"class": "my-class"})
        check = " class: \"my-class\","
        self.assertEqual(str(node.props_to_html()), check)
    def test_pth3(self):
        node = HTMLNode("div", "This is aanother div", None, {"class": "my-class2"})
        check = " class: \"my-class\","
        self.assertNotEqual(str(node.props_to_html()), check)
    def test_pth4(self):
        node = HTMLNode("div", "This is a div", None, {"class": "my-class2"})
        check = " class: \"my-class2\","
        self.assertEqual(str(node.props_to_html()), check)
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_div(self):
        node = LeafNode("div", "This is a div", {"class": "my-class"})
        self.assertEqual(node.to_html(), "<div class: \"my-class\",>This is a div</div>")
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "This is a div", {"class": "my-class"})
        self.assertEqual(node.to_html(), "This is a div")


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(tag = "div", children = [child_node])
        print(parent_node.to_html())
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode(tag = "span", children = [grandchild_node])
        parent_node = ParentNode(tag = "div", children = [child_node])
        print(parent_node.to_html())
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )

    def test_to_html_with_greatgrandchildren(self):
        greatgrandchild_node = LeafNode("i", "greatgrandchild")
        grandchild_leaf_node = LeafNode(None, value = "grandchild")
        grandchild_node = ParentNode(tag="b", children = [grandchild_leaf_node, greatgrandchild_node])
        child_node = ParentNode(tag = "span", children = [grandchild_node])
        parent_node = ParentNode(tag = "div", children = [child_node])
        print(parent_node.to_html())
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild<i>greatgrandchild</i></b></span></div>",
    )


    def test_text1(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")




    def test_text2(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic node")




    def test_text3(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertNotEqual(html_node.tag, "i")
        self.assertNotEqual(html_node.value, "This is a italic node")