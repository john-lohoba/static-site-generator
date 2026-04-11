import os
import shutil
from block_to_html import markdown_to_html_node
from markdown_blocks import BlockType, markdown_to_blocks, block_to_block_type


def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# ") and block_to_block_type(block) == BlockType.HEADING:
            return block.strip("#").strip()
    raise Exception("Markdown has no h1 heading")


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_path_content = open(from_path).read()
    template_path_content = open(template_path).read()

    path_content_to_html = markdown_to_html_node(from_path_content).to_html()
    page_title = extract_title(from_path_content)

    copy_template = template_path_content.replace("{{ Title }}", page_title)
    copy_template = copy_template.replace("{{ Content }}", path_content_to_html)
    copy_template = copy_template.replace('href="/', f'href="{basepath}')
    copy_template = copy_template.replace('src="/', f'src="{basepath}')

    dest_dir_path = os.path.dirname(dest_path)
    os.makedirs(dest_dir_path, exist_ok=True)
    file = open(dest_path, "w")
    file.write(copy_template)
    file.close()

    return


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if not os.path.exists(dir_path_content):
        raise Exception(f"Invalid content path: {dir_path_content}")

    for filename in os.listdir(dir_path_content):
        current_path = os.path.join(dir_path_content, filename)
        if not os.path.isfile(current_path):
            next_path = os.path.join(dir_path_content, filename)
            dest_dir_path_next = os.path.join(dest_dir_path, filename)
            generate_pages_recursive(
                next_path, template_path, dest_dir_path_next, basepath
            )
        else:
            filename_to_html = filename.split(".")[0] + ".html"
            dest_path = os.path.join(dest_dir_path, filename_to_html)
            generate_page(current_path, template_path, dest_path, basepath)
    return
