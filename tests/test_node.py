#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

from unittest import TestCase

from amzlist import Node

from nose.tools import raises

class NodeTest(TestCase):
    """ Test the Node """

    @raises(TypeError)
    def test_no_data(self):
        """ Test instantiation of a Node """
        Node()

    @raises(TypeError)
    def test_next_not_node(self):
        """ Test instantiation of a Node """
        a = Node("A")
        a.next = "B"

    def test_to_str(self):
        """ Test instantiation of a Node """
        b = Node("B")
        a = Node("A")
        a.next = b

        self.assertEqual("A->B", str(a))