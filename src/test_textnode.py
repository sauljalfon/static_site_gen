import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("Node Text 3", TextType.TEXT)

        self.assertEqual(node, node2)
        self.assertNotEqual(node.text, node3.textype)
        self.assertEqual(node.text, node2.text)
        self.assertEqual(node.textype, node2.textype)
        self.assertEqual(node.url, node2.url)

    def test_text_node_to_html(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(text_node_to_html_node(node), LeafNode("b", "This is a text node"))

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")



if __name__ == "__main__":
    unittest.main()
