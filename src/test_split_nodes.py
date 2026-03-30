import unittest

from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text node ` with code `", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)

        self.assertEqual(new_nodes[1].text_type, TextType.CODE_TEXT)

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is text node ** with bold text **", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)

        self.assertEqual(new_nodes[1].text_type, TextType.BOLD_TEXT)

    def test_split_nodes_delimiter_italic(self):
        node = TextNode("This is text node _with italic text_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)

        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC_TEXT)

