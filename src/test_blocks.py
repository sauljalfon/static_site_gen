import unittest

from blocks import (
    BlockType,
    block_to_block_type,
    markdown_to_blocks,
    markdown_to_html_node,
)


class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_markdown_to_html_node(self):
        md = """
        # This is a heading

        This is a paragraph with **bold** text and `code` here
        """
        html_node = markdown_to_html_node(md)
        self.assertEqual(html_node.tag, "div")
        self.assertEqual(len(html_node.children), 2)
        self.assertEqual(html_node.children[0].tag, "h1")
        self.assertEqual(html_node.children[1].tag, "p")

    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

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


class TestMarkdownToBlocks(unittest.TestCase):
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
        self.assertEqual(block_to_block_type("# "), BlockType.heading)
        self.assertEqual(block_to_block_type("```"), BlockType.code)
        self.assertEqual(block_to_block_type("> "), BlockType.quote)
        self.assertEqual(block_to_block_type("- "), BlockType.unordered_list)
        self.assertEqual(block_to_block_type("1. "), BlockType.ordered_list)
        self.assertEqual(block_to_block_type(""), BlockType.paragraph)
