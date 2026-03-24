from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, tex_type, url=None):
        self.text = text
        self.tex_type = tex_type
        self.url = url

    def __eq__(self, other):
        if (
            self.text == other.text
            and self.tex_type == other.tex_type
            and self.url == other.url
        ):
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.tex_type}, {self.url})"
