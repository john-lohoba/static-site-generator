from typing import Text
import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a an italic text node", TextType.ITALIC_TEXT)
        node2 = TextNode("This is a link node", TextType.LINK, url="https://boot.dev")
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a link node", TextType.LINK)
        self.assertFalse(node.url)


if __name__ == "__main__":
    unittest.main()
