from enum import Enum

from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, textype: TextType, url: str | None = None) -> None:
        self.text = text
        self.textype = textype
        self.url = url

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TextNode):
            return False

        return (
            self.text == other.text
            and self.textype == other.textype
            and self.url == other.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.textype}, {self.url})"

def text_node_to_html_node(node: TextNode) -> LeafNode:
    if node.textype == TextType.TEXT:
        return LeafNode(None, node.text)
    elif node.textype == TextType.BOLD:
        return LeafNode("b", node.text)
    elif node.textype == TextType.ITALIC:
        return LeafNode("i", node.text)
    elif node.textype == TextType.CODE:
        return LeafNode("code", node.text)
    elif node.textype == TextType.LINK:
        return LeafNode("a", node.text, {"href": node.url})
    elif node.textype == TextType.IMAGE:
        return LeafNode("img", None, {"src": node.url, "alt": node.text})
    else:
        raise ValueError(f"Invalid text type: {node.textype}")
