import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq_none_url(self):
        node = HTMLNode("h1", "Hello world")
        self.assertEqual("h1", node.tag)