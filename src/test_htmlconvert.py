import unittest
from htmlconvert import markdown_to_html_node

class TestMarkdownToHtmlNode(unittest.TestCase):

    def test_paragraphs(self):
        md = """
This is a
standard paragraph

```
this is code
```

# This is another paragraph with _italic_ text and `code` here

### This is the same paragraph on a new line

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
        
        node = markdown_to_html_node(md)
        #html = node.to_html()
        #self.assertEqual(
        #    html,
        #    "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        #)


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
        
    def test_codeblock2(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )



if __name__ == "__main__":
    unittest.main()