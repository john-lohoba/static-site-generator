import os
import shutil

from copystatic import copy_files_recursive, generate_page, generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./public"

from_path = "./content/index.md"
template_path = "./template.html"
dest_path = "./public/index.html"

dir_path_content = "./content"
template_path = "./template.html"
dest_dir_path = "./public"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    generate_pages_recursive(dir_path_content, template_path, dest_dir_path)


main()
