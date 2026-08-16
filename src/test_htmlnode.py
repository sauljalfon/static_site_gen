import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode("div", "Hello, World!", None, None)
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello, World!")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_leaf_node_init(self):
        node = LeafNode("p", "This is a paragraph.")
        node2 = LeafNode("p", "Hello, world!")
        self.assertEqual(node2.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a paragraph.")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)


class TestParentNode(unittest.TestCase):
    def test_parent_node_init(self):
        node = ParentNode("div", [LeafNode("p", "This is a paragraph.")])
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.children, [LeafNode("p", "This is a paragraph.")])
        self.assertEqual(node.props, None)
        self.assertEqual(node.to_html(), "<div><p>This is a paragraph.</p></div>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
