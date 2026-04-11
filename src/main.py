import os
import shutil
import sys

from copystatic import copy_files_recursive, generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./docs"

dir_path_content = "./content"
template_path = "./template.html"
dest_dir_path = "./docs"


if len(sys.argv) == 1:
    basepath = "/"
else:
    basepath = sys.argv[1]


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath)


main()
