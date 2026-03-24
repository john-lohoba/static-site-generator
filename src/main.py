from textnode import TextNode, TextType


def main():
    example_node = TextNode(
        "This is some anchor text", TextType.LINK, "https://boot.dev"
    )
    print(example_node)


main()
