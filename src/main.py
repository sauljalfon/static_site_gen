import os
import shutil

from generator import generate_pages_recursive


def main():
    source_dir_to_dest_dir("static", "public")
    generate_pages_recursive("content", "template.html", "public")


def source_dir_to_dest_dir(source_dir: str, dest_dir: str) -> None:
    if not os.path.exists(dest_dir):
        raise RuntimeError(f"Destination directory {dest_dir} does not exist")

    shutil.rmtree(dest_dir)
    shutil.copytree(source_dir, dest_dir)
    print(f"Copied {source_dir} to {dest_dir}")


if __name__ == "__main__":
    main()
