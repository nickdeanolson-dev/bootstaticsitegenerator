import unittest
from html import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_pth1(self):
        pass
    def test_pth2(self):
        node = HTMLNode("div", "This is aanother div", None, {"class": "my-class"})
        print(str(node.props_to_html()))
        check = " class: \"my-class\","
        self.assertEqual(str(node.props_to_html()), check)
    def test_pth3(self):
        node = HTMLNode("div", "This is aanother div", None, {"class": "my-class2"})
        print(str(node.props_to_html()))
        check = " class: \"my-class\","
        self.assertNotEqual(str(node.props_to_html()), check)
    def test_pth4(self):
        node = HTMLNode("div", "This is a div", None, {"class": "my-class2"})
        print(str(node.props_to_html()))
        check = " class: \"my-class2\","
        self.assertEqual(str(node.props_to_html()), check)

