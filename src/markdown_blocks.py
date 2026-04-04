from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    split_blocks = markdown.split("\n\n")
    new_list = []
    for block in split_blocks:
        block = block.strip()
        if block != "":
            new_list.append(block)
    return new_list


def block_to_block_type(markdown_text_block):
    split_block = markdown_text_block.split("\n")

    if markdown_text_block.startswith(
        ("# ", "## ", "### ", "#### ", "##### ", "###### ")
    ):
        return BlockType.HEADING

    if len(split_block) > 1 and split_block[0] == "```" and split_block[-1] == "```":
        return BlockType.CODE

    quote = True
    unordered_list = True
    ordered_list = True
    n = 1
    for line in split_block:
        if not line.startswith(">"):
            quote = False
        if not line.startswith("- "):
            unordered_list = False
        if not line.startswith(f"{n}. "):
            # print(f"{n}.")
            ordered_list = False
        n += 1

    if quote is True:
        return BlockType.QUOTE
    if unordered_list is True:
        return BlockType.UNORDERED_LIST
    if ordered_list is True:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
