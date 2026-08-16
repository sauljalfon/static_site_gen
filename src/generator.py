import os

from blocks import markdown_to_html_node


def extract_title(markdown: str):
    if markdown.startswith("# "):
        return markdown[2:]
    raise ValueError("No title found")


def generator_page(from_path: str, template_path: str, dest_path: str, basepath: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    basepath = basepath.rstrip("/")
    markdown = open(from_path).read()
    template = open(template_path).read()
    html = markdown_to_html_node(markdown)
    html_str = html.to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_str)
    template = template.replace('href="/', f'href="{basepath}/')
    template = template.replace('src="/', f'src="{basepath}/')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    open(dest_path, "w").write(template)


def generate_pages_recursive(
    dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str = "/"
):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        if os.path.isfile(from_path):
            if from_path.endswith(".md"):
                dest_path = dest_path.removesuffix(".md") + ".html"
                generator_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)
