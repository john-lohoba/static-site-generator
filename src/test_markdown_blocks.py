import unittest
from markdown_blocks import BlockType, markdown_to_blocks, block_to_block_type


class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
        md = """
# This is a heading paragraph

This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

> This is a quote paragrapgh
> with some more text

```
This is a code paragraph
```

- This is an unordered list
- with items

1. This is an ordered list
2. With a second item
3. And a third one

###### This is a heading paragraph
"""
        markdown_text_blocks = markdown_to_blocks(md)
        blocks = []
        for block in markdown_text_blocks:
            blocks.append(block_to_block_type(block))
        self.assertEqual(blocks[0], BlockType.HEADING)
        self.assertEqual(blocks[1], BlockType.PARAGRAPH)
        self.assertEqual(blocks[2], BlockType.PARAGRAPH)
        self.assertEqual(blocks[3], BlockType.QUOTE)
        self.assertEqual(blocks[4], BlockType.CODE)
        self.assertEqual(blocks[5], BlockType.UNORDERED_LIST)
        self.assertEqual(blocks[6], BlockType.ORDERED_LIST)
        self.assertEqual(blocks[7], BlockType.HEADING)
