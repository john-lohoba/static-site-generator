import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TextHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(
            "h1",
            "This is a heading",
        )
        repr = "HTMLNode tag=h1, value=This is a heading, children=None, props=None"
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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_lead_to_html_a(self):
        node = LeafNode("a", "This is a link", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">This is a link</a>'
        )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
