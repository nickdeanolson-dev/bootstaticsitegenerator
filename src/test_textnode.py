import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eq2(self):
        node = TextNode("this contains a ' character", TextType.ITALIC)
        node2 = TextNode("this contains a ' character", TextType.ITALIC, url=None)
        self.assertEqual(node, node2)
    def test_neq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("this contains a ' character", TextType.ITALIC, url=None)
        self.assertNotEqual(node, node2)
    def test_neq2(self):
        node = TextNode("This is some anchor text", TextType.BOLD, "https://boot.dev")
        node2 = TextNode("this contains a ' character", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_neq3(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()