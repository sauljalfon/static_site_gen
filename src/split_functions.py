from textnode import TextNode, TextType
from regex_functions import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.textype != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        images = extract_markdown_images(old_node.text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        remaining_text = old_node.text
        for alt_text, url in images:
            markdown = f"![{alt_text}]({url})"
            parts = remaining_text.split(markdown, 1)

            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.TEXT))

            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            remaining_text = parts[1]

        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.textype != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        links = extract_markdown_links(old_node.text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue

        remaining_text = old_node.text
        for anchor_text, url in links:
            markdown = f"[{anchor_text}]({url})"
            parts = remaining_text.split(markdown, 1)

            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.TEXT))

            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            remaining_text = parts[1]

        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.textype == TextType.TEXT:
            split_text = old_node.text.split(delimiter)
            if len(split_text) % 2 == 0:
                raise ValueError("Invalid markdown syntax")

            for i, text in enumerate(split_text):
                if text == "":
                    continue

                new_nodes.append(TextNode(text, text_type if i % 2 == 1 else TextType.TEXT))
        else:
            new_nodes.append(old_node)
    return new_nodes
