import os
import shutil
import sys

from generator import generate_pages_recursive


def main():

    basepath = sys.argv[1] if len(sys.argv) > 1 else ""

    source_dir_to_dest_dir("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)


def source_dir_to_dest_dir(source_dir: str, dest_dir: str) -> None:
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    shutil.rmtree(dest_dir)
    shutil.copytree(source_dir, dest_dir)
    print(f"Copied {source_dir} to {dest_dir}")


if __name__ == "__main__":
    main()
