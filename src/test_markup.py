import unittest
from markup import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
from blockmarkup import BlockType, markdown_to_blocks, block_to_block_type
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

    def test_img1(self):
        text = "Test line with an embedded ![This is an image](https://i.imgur.com/aKaOqIh.gif) image reference"
        answer = extract_markdown_images(text)
        if len(answer) > 0:
            self.assertEqual(answer[0][0], "This is an image")
            self.assertEqual(answer[0][1], "https://i.imgur.com/aKaOqIh.gif")

    def test_link1(self):
        text = "Test line with an embedded [This is an image](https://i.imgur.com/aKaOqIh.gif) link reference"
        answer = extract_markdown_links(text)
        if len(answer) > 0:
            self.assertEqual(answer[0][0], "This is an image")
            self.assertEqual(answer[0][1], "https://i.imgur.com/aKaOqIh.gif")

    def test_img2(self):
        text = "![This is an image](https://i.imgur.com/aKaOqIh.gif) image reference"
        answer = extract_markdown_images(text)
        if len(answer) > 0:
            self.assertEqual(answer[0][0], "This is an image")
            self.assertEqual(answer[0][1], "https://i.imgur.com/aKaOqIh.gif")

    def test_link2(self):
        text = "[This is an image](https://i.imgur.com/aKaOqIh.gif) link reference"
        answer = extract_markdown_links(text)
        if len(answer) > 0:
            self.assertEqual(answer[0][0], "This is an image")
            self.assertEqual(answer[0][1], "https://i.imgur.com/aKaOqIh.gif")

    def test_linkNeq1(self):
        text = "Test line with an embedded ![This is an image](https://i.imgur.com/aKaOqIh.gif) link reference"
        answer = extract_markdown_links(text)
        if len(answer) > 0:
            self.assertNotEqual(answer[0][0], "This is an image")
            self.assertNotEqual(answer[0][1], "https://i.imgur.com/aKaOqIh.gif")



    def test_splitimage1(self):
        text = TextNode("A text ![B image](https://i.imgur.com/aKaOqIh.gif) C text", TextType.TEXT)
        result = (split_nodes_image([text]))
        self.assertListEqual(
            [
                TextNode("A text ", TextType.TEXT),
                TextNode("B image", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" C text", TextType.TEXT),
            ],
            result,
        )



    def test_splitimage2(self):
        text = TextNode("A Line ![B image](https://i.imgur.com/aKaOqIh.gif) C line ![D image](https://i.imgur.com/aKaOqIh.png)", TextType.TEXT)
        result = (split_nodes_image([text]))
        self.assertListEqual(
            [
                TextNode("A Line ", TextType.TEXT),
                TextNode("B image", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" C line ", TextType.TEXT),
                TextNode("D image", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.png"),
            ],
            result,
        )


    def test_splitlink1(self):
        text = TextNode("A text [B link](https://i.imgur.com/aKaOqIh.gif) C text", TextType.TEXT)
        result = (split_nodes_link([text]))
        self.assertListEqual(
            [
                TextNode("A text ", TextType.TEXT),
                TextNode("B link", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" C text", TextType.TEXT),
            ],
            result,
        )



    def test_splitlink2(self):
        text = TextNode("A Line [B link](https://i.imgur.com/aKaOqIh.gif) C line [D link](https://i.imgur.com/aKaOqIh.png)", TextType.TEXT)
        result = (split_nodes_link([text]))
        self.assertListEqual(
            [
                TextNode("A Line ", TextType.TEXT),
                TextNode("B link", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" C line ", TextType.TEXT),
                TextNode("D link", TextType.LINK, "https://i.imgur.com/aKaOqIh.png"),
            ],
            result,
        )


    def test_splitlink3(self):
        text = TextNode("A Line [B link](https://i.imgur.com/aKaOqIh.gif) C line [B link repeated](https://i.imgur.com/aKaOqIh.gif)[D link](https://i.imgur.com/aKaOqIh.png) and end text ", TextType.TEXT)
        result = (split_nodes_link([text]))
        self.assertListEqual(
            [
                TextNode("A Line ", TextType.TEXT),
                TextNode("B link", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" C line ", TextType.TEXT),
                TextNode("B link repeated", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode("D link", TextType.LINK, "https://i.imgur.com/aKaOqIh.png"),
                TextNode(" and end text ", TextType.TEXT),
            ],
            result,
        )

    def test_texttonodes1(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            result,
        )



    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


    def test_block_to_block_type(self):
        md = """
This is a
standard paragraph

```
this is code
```

# This is another paragraph with _italic_ text and `code` here

# This is the same paragraph on a new line

- unordered list a
- unordered list b

- broken UL list a
> broken UL list b

> quote block line 1
> quote block line 2

> quote block line 1
broken quote block line 2

1. This is a list
2. with items
3. test

1. broken numbered list
3. out of order

1. broken numbered list
2 off format

1. . double digits
2. . double digits
3. double digits
4. double digits
5. double digits. double digits
6. double digits
7. double digits
8. double digits
9. double digits
10. double digits
"""

        blocks = markdown_to_blocks(md)
        results = []
        for b in blocks:
            results.append(block_to_block_type(b))
        
        self.assertEqual(
            results,
            [
                BlockType.PARAGRAPH,
                BlockType.CODE,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.UNORDERED_LIST,
                BlockType.PARAGRAPH,
                BlockType.QUOTE,
                BlockType.PARAGRAPH,
                BlockType.ORDERED_LIST,
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
                BlockType.ORDERED_LIST,
            ],
        )



if __name__ == "__main__":
    unittest.main()