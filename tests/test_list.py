#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

from unittest import TestCase
from nose.tools import raises

from amzlist import LinkedList
from amzlist import Node

class ListTest(TestCase):
    """ Test the linked list """

    def setUp(self):
        self.linked_list = LinkedList()

    def test_insert(self):
        """ Test """
        self.linked_list.append(10)
        self.assertEqual(1, len(self.linked_list))

        # prepend a Node
        node_a = Node("a")
        self.linked_list.prepend(node_a)
        self.assertEqual(2, len(self.linked_list))

        # prepend an int
        self.linked_list.prepend(20)
        self.assertEqual(3, len(self.linked_list))

        # insert a Node
        node_b = Node("b")
        self.linked_list.insert(node_b, node_a)
        self.assertEqual(4, len(self.linked_list))

        # insert a float
        self.linked_list.insert(35.5, node_b)
        self.assertEqual(5, len(self.linked_list))

        # test the order of the Nodes
        values = [20, "a", "b", 35.5, 10]
        node = self.linked_list
        for value in values:
            self.assertEqual(value, node.data)
            node = node.next

    @raises(TypeError)
    def test_insert_none(self):
        """ Test inserting a Node after a parameter that is not a Node. """
        self.linked_list.insert(35.5, None)

    def test_remove(self):
        """ Test removal. """

        # initialize the list with Nodes
        node_10 = Node(10)
        self.linked_list.append(node_10)
        node_20 = Node(20)
        self.linked_list.append(node_20)
        node_30 = Node(30)
        self.linked_list.append(node_30)

        # make sure the Nodes are correct
        self.assertEqual(3, len(self.linked_list))
        values = [10, 20, 30]
        node = self.linked_list
        for value in values:
            self.assertEqual(value, node.data)
            node = node.next

        # remove a Node
        self.linked_list.remove(node_20)

        # make sure the Node has been removed and the
        # order is correct
        self.assertEqual(2, len(self.linked_list))
        values = [10, 30]
        node = self.linked_list
        for value in values:
            self.assertEqual(value, node.data)
            node = node.next

        # remove another Node
        self.linked_list.remove(10)

        # make sure the Node has been removed and the
        # order is correct
        self.assertEqual(1, len(self.linked_list))
        values = [30]
        node = self.linked_list
        for value in values:
            self.assertEqual(value, node.data)
            node = node.next

        # remove last Node
        self.linked_list.remove(30)

        # make sure it has been removed
        self.assertEqual(0, len(self.linked_list))

    @raises(ValueError)
    def test_remove_unknown(self):
        # try to remove a Node that is not in the list
        self.linked_list.remove("A")


    def test_first_and_last(self):
        """ Test the first_node attribute and the last_node property. """
        lnkd_list = self.linked_list

        self.assertTrue(lnkd_list.first_node is None)
        self.assertTrue(lnkd_list.last_node is None)

        node_10 = Node(10)
        lnkd_list.append(node_10)

        self.assertFalse(lnkd_list.first_node is None)
        self.assertFalse(lnkd_list.last_node is None)
        self.assertEqual(lnkd_list.first_node, lnkd_list.last_node)

        node_10 = Node(10)
        lnkd_list.append(node_10)
        self.assertNotEqual(lnkd_list.first_node, lnkd_list.last_node)

    def test_find_data(self):
        """ Test the find method based on a Node's data """
        lnkd_list = self.linked_list

        values = [1, 2, 3, 4, 5]
        # reverse them as they are being prepended so
        # the order will be A->B->C->D->E
        for val in reversed(values):
            lnkd_list.prepend(val)

        # validate it found the correct Node by checking the
        # it's data and the data of the next Node.
        node = lnkd_list.find(3)
        self.assertEqual(3, node.data)
        self.assertEqual(4, node.next.data)

    def test_find_data_N(self):
        """ Test the find method based on a Node's data and where two Node's
        have the same data being searched for. """
        lnkd_list = self.linked_list

        values = ['A', 1, 2, 3, 'A', 5]
        # reverse them as they are being prepended so
        # the order will be A->B->C->D->E
        for val in reversed(values):
            lnkd_list.prepend(val)

        # validate it found the correct Node by checking the
        # it's data and the data of the next Node.
        node = lnkd_list.find('A')
        self.assertEqual('A', node.data)
        self.assertEqual(1, node.next.data)

    def test_to_string(self):
        """ Test the string rep is correct. """
        lnkd_list = self.linked_list

        values = ['A', 'B', 'C', 'D', 'E', 'F']
        for val in reversed(values):
            lnkd_list.prepend(val)

        self.assertEqual('A->B->C->D->E->F', str(lnkd_list))

    def test_reverse_iterative(self):
        """ Test reversing a list iteratively. """
        lnkd_list = self.linked_list

        values = ['A', 'B', 'C', 'D', 'E']

        # reverse them as they are being prepended so
        # the order will be A->B->C->D->E
        for val in reversed(values):
            lnkd_list.prepend(val)

        new_list = lnkd_list.reverse_iterative()
        self.assertEqual(5, len(new_list))

        # reverse them as the order of the reversed list 
        # will be E->D->C->B->A
        node = new_list
        for value in reversed(values):
            self.assertEqual(value, node.data)
            node = node.next

        self.assertEqual(lnkd_list.first_node.data, new_list.last_node.data)

    def test_reverse_recursive(self):
        """ Test reversing a list recursively. """
        lnkd_list = self.linked_list

        values = ['A', 'B', 'C', 'D', 'E']
        for val in reversed(values):
            lnkd_list.prepend(val)

        new_list = lnkd_list.reverse_recursive()
        self.assertEqual(5, len(new_list))

        # reverse them as the order of the reversed list 
        # will be E->D->C->B->A
        node = new_list
        for value in reversed(values):
            self.assertEqual(value, node.data)
            node = node.next

        self.assertEqual(lnkd_list.first_node.data, new_list.last_node.data)

    def test_reverse_i_empty(self):
        """ Test reversing an empty list iteratively. """
        lnkd_list = self.linked_list
        new_list = self.linked_list.reverse_iterative()
        self.assertEqual(0, len(new_list))

    def test_reverse_r_empty(self):
        """ Test reversing an empty list recursively. """
        lnkd_list = self.linked_list
        new_list = self.linked_list.reverse_recursive()
        self.assertEqual(0, len(new_list))

    def test_push_pop(self):
        lnkd_list = self.linked_list
        self.assertEqual(0, len(lnkd_list))

        lnkd_list.push("Item 1")
        lnkd_list.push("Item 2")
        self.assertEqual(2, len(lnkd_list))

        node = lnkd_list.pop()
        self.assertEqual("Item 2", node.data)
        self.assertEqual(1, len(lnkd_list))



class CycleTest(TestCase):

    def setUp(self):
        # initialize the list with Nodes
        lnkd_list = LinkedList(strict=True)
        self.node_john = Node('John')
        lnkd_list.append(self.node_john)
        self.node_james = Node('James')
        lnkd_list.append(self.node_james)
        self.node_joe = Node('Joe')
        lnkd_list.append(self.node_joe)
        self.lnkd_list = lnkd_list

    @raises(ValueError)
    def test_cycle_immediate(self):
        """ Test to make sure cycle detection is working. """
        # create another node, Jules. Point it's next at John, and
        # John's next at Jules.
        # John -> Jules -> John
        node_jules = Node('Jules')
        self.node_john.next = node_jules
        node_jules.next = self.node_john

    @raises(ValueError)
    def test_cycle_removed(self):
        """ Test to make sure cycle detection is working. """
        # create another node, Jules. Point it's next at John, and
        # James's next at Jules. Joe is orpaned.
        # John -> James -> Jules -> John | None -> Joe -> None
        node_jules = Node('Jules')
        self.node_james.next = node_jules
        node_jules.next = self.node_john

class ManyNodesTest(TestCase):

    def test_many(self):
        """ Tests the list can handle a large number of Nodes. """
        lnkd_list = LinkedList()
        for i in range(2**16):
            lnkd_list.prepend(i)
        self.assertEqual(2**16, lnkd_list.data + 1)
