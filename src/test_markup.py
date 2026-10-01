import unittest
from markup import split_nodes_delimiter
from textnode import TextNode, TextType


class TestMarkupNode(unittest.TestCase):



    def test_eq1(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        node1 = TextNode("This is text with a ", TextType.TEXT)
        node2 = TextNode("code block", TextType.CODE)
        node3 = TextNode(" word", TextType.TEXT)
        self.assertEqual(new_nodes[0], node1)
        self.assertEqual(new_nodes[1], node2)
        self.assertEqual(new_nodes[2], node3)

    def test_neq1(self):
        node = TextNode("`This is text with a` coode at the start word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        node1 = TextNode("This is text with a ", TextType.TEXT)
        node2 = TextNode("code block", TextType.CODE)
        node3 = TextNode(" word", TextType.TEXT)
        self.assertNotEqual(new_nodes[0], node1)
        self.assertNotEqual(new_nodes[1], node2)
        self.assertNotEqual(new_nodes[2], node3)
    
    def test_eq2(self):
        node = TextNode("`This is text with a` coode at the start word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        node1 = TextNode("", TextType.TEXT)
        node2 = TextNode("This is text with a", TextType.CODE)
        node3 = TextNode(" coode at the start word", TextType.TEXT)
        self.assertEqual(new_nodes[0], node1)
        self.assertEqual(new_nodes[1], node2)
        self.assertEqual(new_nodes[2], node3)

    
    def test_eq3(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.ITALIC)
        node1 = TextNode("This is text with a ", TextType.TEXT)
        node2 = TextNode("bold block", TextType.ITALIC)
        node3 = TextNode(" word", TextType.TEXT)
        self.assertEqual(new_nodes[0], node1)
        self.assertEqual(new_nodes[1], node2)
        self.assertEqual(new_nodes[2], node3)

    
    def test_eq4(self):
        node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        node1 = TextNode("This is text with a ", TextType.TEXT)
        node2 = TextNode("italic block", TextType.ITALIC)
        node3 = TextNode(" word", TextType.TEXT)
        self.assertEqual(new_nodes[0], node1)
        self.assertEqual(new_nodes[1], node2)
        self.assertEqual(new_nodes[2], node3)


    
    def test_eq5(self):
        nodelist = []
        nodelist.append(TextNode("TTThis is text with a `code block` word", TextType.TEXT))
        nodelist.append(TextNode("`This is text with a` coode at the start word", TextType.TEXT))
        nodelist.append(TextNode("This is text with a **bold block** word", TextType.TEXT))
        nodelist.append(TextNode("This is text with a _italic block_ word", TextType.TEXT))
        new_nodes = split_nodes_delimiter(nodelist, "**", TextType.BOLD)
        node1 = TextNode("This is text with a ", TextType.TEXT)
        node2 = TextNode("bold block", TextType.BOLD)
        node3 = TextNode(" word", TextType.TEXT)
        self.assertEqual(new_nodes[2], node1)
        self.assertEqual(new_nodes[3], node2)
        self.assertEqual(new_nodes[4], node3)

    
    def test_eq6(self):
        nodelist = []
        nodelist.append(TextNode("TTThis is text with a `code block` word", TextType.TEXT))
        nodelist.append(TextNode("`This is text with a` coode at the start word", TextType.TEXT))
        nodelist.append(TextNode("This is text with a **bold block** word", TextType.TEXT))
        nodelist.append(TextNode("This is text with a _italic block_ word", TextType.TEXT))
        new_nodes = split_nodes_delimiter(nodelist, "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
        node1 = TextNode("This is text with a ", TextType.TEXT)
        node2 = TextNode("bold block", TextType.BOLD)
        node3 = TextNode(" word", TextType.TEXT)
        node4 = TextNode("", TextType.TEXT)
        node5 = TextNode("This is text with a", TextType.CODE)
        node6 = TextNode(" coode at the start word", TextType.TEXT)
        self.assertEqual(new_nodes[6], node1)
        self.assertEqual(new_nodes[7], node2)
        self.assertEqual(new_nodes[8], node3)
        self.assertEqual(new_nodes[3], node4)
        self.assertEqual(new_nodes[4], node5)
        self.assertEqual(new_nodes[5], node6)




if __name__ == "__main__":
    unittest.main()