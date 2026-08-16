from enum import Enum

from htmlnode import HTMLNode, LeafNode, ParentNode
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.paragraph:
            text = " ".join(block.split("\n"))
            children.append(ParentNode("p", text_to_children(text)))
        elif block_type == BlockType.heading:
            heading_level = len(block) - len(block.lstrip("#"))
            text = block[heading_level + 1:]
            children.append(ParentNode(f"h{heading_level}", text_to_children(text)))
        elif block_type == BlockType.code:
            text = block.removeprefix("```").removesuffix("```").lstrip()
            code_node = text_node_to_html_node(TextNode(text, TextType.CODE))
            children.append(ParentNode("pre", [code_node]))
        elif block_type == BlockType.quote:
            text = "\n".join(line.removeprefix("> ") for line in block.split("\n"))
            children.append(ParentNode("blockquote", text_to_children(text)))
        elif block_type == BlockType.unordered_list:
            list_items = []
            for line in block.split("\n"):
                text = line.removeprefix("- ")
                list_items.append(ParentNode("li", text_to_children(text)))
            children.append(ParentNode("ul", list_items))
        elif block_type == BlockType.ordered_list:
            list_items = []
            for line in block.split("\n"):
                text = line.split(". ", 1)[1]
                list_items.append(ParentNode("li", text_to_children(text)))
            children.append(ParentNode("ol", list_items))
    return ParentNode("div", children)


def text_to_children(text) -> list[HTMLNode]:
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]


class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"


def block_to_block_type(block: str) -> BlockType:
    if block.startswith("#"):
        return BlockType.heading
    if block.startswith("```"):
        return BlockType.code
    if block.startswith("> "):
        return BlockType.quote
    if block.startswith("- "):
        return BlockType.unordered_list
    if block.startswith("1. "):
        return BlockType.ordered_list
    return BlockType.paragraph


def markdown_to_blocks(markdown: str):
    blocks = markdown.split("\n\n")
    blocks = [
        "\n".join(line.strip() for line in block.strip().split("\n"))
        for block in blocks
        if block.strip() != ""
    ]
    return blocks
