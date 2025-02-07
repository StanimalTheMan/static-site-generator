import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq_none_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://link1")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://link1")
        self.assertEqual(node, node2)

    def test_not_eq_text_type(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_text_url(self):
        node = TextNode("This is a text node", TextType.CODE, "https://link1")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://link2")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()