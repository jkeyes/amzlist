#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

class Node(object):
    """ A Node is a simple object with two attributes, next and data.

    Data stores the content, and next holds a reference to another Node.
    """

    def __init__(self, data):
        """ Initialize a new Node with the specified data. """

        self.next = None
        """ Next text """

        self.data = data
        """ Data text """

    def __setattr__(self, key, value):
        """ Override __setattr__ to ensure that next is a Node. """
        if key == "next":
            if value is not None:
                if not isinstance(value, Node):
                    raise TypeError
        super(Node, self).__setattr__(key, value)

    def __str__(self):
        """ Returns the string representation e.g. A->None, or A->B. """
        next = self.next.data if self.next else "None"
        return "%s->%s" % (self.data, next)

class LinkedList(object):
    """ A LinkedList implementation. """

    def __init__(self):
        """ Initialize a new LinkedList. """
        super(LinkedList, self).__init__()
        self.first_node = None

    @property
    def next(self):
        """ Returns the next Node. """
        return self.first_node.next

    @property
    def data(self):
        """ Returns the data for the first Node. """
        return self.first_node.data

    @property
    def last_node(self):
        """ Returns the last Node. """
        nodes = self.as_list()
        if nodes:
            return nodes[-1]
        return None

    def prepend(self, node):
        """ Insert a Node at the head. """
        if not isinstance(node, Node):
            node = Node(node)

        node.next = self.first_node
        self.first_node = node

    def append(self, node):
        """ Insert a Node at the tail. """
        if not isinstance(node, Node):
            node = Node(node)

        if self.first_node is None:
            self.first_node = node
        else:
            self.last_node.next = node

    def insert(self, node, after):
        """ Insert a Node after the specified Node. """
        if not isinstance(after, Node):
            raise TypeError("After must be a Node not a %s" % (type(after)))

        if not isinstance(node, Node):
            node = Node(node)

        node.next = after.next
        after.next = node

    def remove(self, node):
        """ Remove the specified Node. If the Node has data and
        next a specific match is used. If the node parameter is 
        data then the first node with equal data is removed. """
        curr, prev = self.find(node, inc_prev=True)
        if curr:
            self._remove(curr, prev)

    def find(self, node, inc_prev=None):
        """ Find the specified Node. If the Node has data and
        next a specific match is used. If the node parameter is 
        data then the first node with equal data is returned. 

        If inc_prev is True, this method returns the node and 
        it's previous node in a tuple, else it returns the node.

        This method returns None if the node cannot be found.
        """
        if inc_prev is None:
            inc_prev = False
        if not isinstance(node, Node):
            node = Node(node)

        if node.next:
            # match based on Node
            test = lambda curr, node: curr == node
        else:
            # match based on data
            test = lambda curr, node: curr.data == node.data

        prev = None
        curr = self.first_node
        while (curr):
            if test(curr, node):
                # include the previous node in the return value
                if inc_prev:
                    return (curr, prev)
                # just return the node
                else:
                    return curr
            prev = curr
            curr = curr.next
        raise ValueError("Node %s could not be found." % (node.data))

    def _remove(self, curr, prev):
        """ Remove the node curr and update the next attribute for prev. """
        if prev:
            prev.next = curr.next
        else:
            self.first_node = curr.next
        del curr

    def as_list(self):
        """ Returns a list of Nodes. """
        nodes = []
        node = self.first_node
        while node:
            nodes.append(node)
            node = node.next
        return nodes

    def __len__(self):
        """ Returns the lenght/size of the list. """
        return len(self.as_list())

    def __str__(self):
        """ The string representation of the list. """
        return "->".join([str(n.data) for n in self.as_list()])

    def reverse_iterative(self):
        """ Returns another LinkedList but with the Nodes in reverse order. """
        new_list = LinkedList()
        node = self.first_node
        while node:
            next = node.next
            new_list.prepend(node)
            node = next
        return new_list

    def reverse_recursive(self, node=None, new_list=None):
        """ Returns another LinkedList but with the Nodes in reverse order. """
        if new_list is None:
            new_list = LinkedList()
            if node is None:
                node = self.first_node
        if node:
            next = node.next
            new_list.prepend(node)
            if next is not None:
                self.reverse_recursive(next, new_list)
        return new_list
