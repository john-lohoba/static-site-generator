import unittest

from htmlnode import HTMLNode


class TextHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(
            "h1",
            "This is a heading",
        )
        repr = "tag=h1, value=This is a heading, children=None, props=None"
        self.assertEqual(node.__repr__(), repr)

    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "This is a link",
            None,
            {"href": "https://www.google.com", "target": "blank"},
        )
        prop = ' href="https://www.google.com" target="blank"'
        self.assertEqual(node.props_to_html(), prop)

    def test_not_equal_nodes(self):
        node = HTMLNode("p", "This is a paragraph")
        node2 = HTMLNode("h1", "This is a heading")
        self.assertNotEqual(node, node2)
