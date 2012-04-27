#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

class Node(object):
    """ A Node is a simple object with two attributes, `next` and `data`.

    `data` stores a value, and `next` holds a reference to another Node.
    """
    strict = False

    def __init__(self, data):
        """ Initialize a new Node with the specified data. """

        self.next = None
        """ Next text """

        self.data = data
        """ Data text """

    def __setattr__(self, key, value):
        """ Override `__setattr__` to ensure that next is a Node. """
        if key == "next" and value:
            if value is not None:
                if not isinstance(value, Node):
                    raise TypeError

            if Node.strict and value.next:
                # If we are in strict mode we check to make sure this
                # modification to `next` will not create a cycle.
                node = value.next
                while node:
                    if node == self:
                        raise ValueError("Cannot insert %s cycle detected" \
                                % (value.data))
                    node = node.next

        super(Node, self).__setattr__(key, value)

    def __str__(self):
        """ Returns the string representation e.g. A->None, or A->B. """
        next = self.next.data if self.next else "None"
        return "%s->%s" % (self.data, next)

class LinkedList(object):
    """ A LinkedList implementation. """

    def __init__(self, strict=None):
        """ Initialize a new LinkedList. """
        if strict is None:
            strict = False
        Node.strict = strict

        super(LinkedList, self).__init__()
        self.first_node = None

    @property
    def next(self):
        """ Returns the `next` Node. """
        return self.first_node.next

    @property
    def data(self):
        """ Returns the `data` for the first Node. """
        return self.first_node.data

    @property
    def last_node(self):
        """ Returns the last Node. """
        nodes = self.as_list()

        if nodes:
            # If there are nodes return the last one.
            return nodes[-1]
        # No nodes, return None
        return None

    def prepend(self, node):
        """ Inserts `node` at the head of the LinkedList. """
        if not isinstance(node, Node):
            # If the node parameter is not a Node then update it
            # to refer to one.
            node = Node(node)

        # The new node will store the current first_node in it's next attribute.
        node.next = self.first_node
        # Update the first_node reference to the new node.
        self.first_node = node

    def append(self, node):
        """ Inserts `node` at the tail of the LinkedList. """
        if not isinstance(node, Node):
            # If the node parameter is not a Node then update it
            # to refer to one.
            node = Node(node)

        if self.first_node is None:
            # The first_node is None therefore we just set it.
            self.first_node = node
        else:
            # Find the last_node in the list and update it's next attribute.
            self.last_node.next = node

    def insert(self, node, after):
        """ Inserts `node` and makes `after.next` refer to it. """
        if not isinstance(after, Node):
            # If the after parameter is not a Node raise an error.
            raise TypeError("After must be a Node not a %s" % (type(after)))

        if not isinstance(node, Node):
            # If the node parameter is not a Node then update it
            # to refer to one.
            node = Node(node)

        node.next = after.next
        after.next = node

    def push(self, node):
        """ Prepends a Node to the head. """
        self.prepend(node)

    def pop(self):
        """ Returns the Node from the head, and removes it. """
        res = self.first_node
        self.first_node = self.first_node.next
        return res

    def remove(self, node):
        """ Remove the specified `node`. 

        If the `node` parameter is a Node, and it has `data` and 
        a `next` Node then the first Node with encountered that
        has the same `data` and `next` attribute values will be
        removed.

        If the `node` parameter is a value other than a Node or a 
        Node with just a `data` attribute value, then the first node 
        encountered with the same `data` attribute is removed.
        """
        curr, prev = self.find(node, inc_prev=True)
        if curr:
            self._remove(curr, prev)

    def find(self, node, inc_prev=None):
        """ Find the specified Node.

        If the `node` parameter is a Node, and it has `data` and 
        a `next` Node then the first Node with encountered that
        has the same `data` and `next` attribute values will match.

        If the `node` parameter is a value other than a Node or a 
        Node with just a `data` attribute value, then the first node 
        encountered with the same `data` attribute value will match.

        If `inc_prev` is `True`, this method returns the node and 
        it's previous node in a tuple, otherwise it returns the node.

        This method returns `None` if the node cannot be found.
        """
        if inc_prev is None:
            # Default include previous node to False
            inc_prev = False
        if not isinstance(node, Node):
            # If the node parameter is not a Node then update it
            # to refer to one.
            node = Node(node)

        if node.next:
            # match based on Node
            test = lambda curr, node: curr == node
        else:
            # match based on data
            test = lambda curr, node: curr.data == node.data

        prev = None
        curr = self.first_node

        # Iterate over each node.
        while curr:
            if test(curr, node):
                # include the previous node in the return value
                if inc_prev:
                    return (curr, prev)
                # just return the node
                else:
                    return curr
            prev = curr
            curr = curr.next

        # No node could be found.
        raise ValueError("Node %s could not be found." % (node.data))

    def _remove(self, curr, prev):
        """ Remove `curr` and update the next attribute for `prev`. """
        if prev:
            # If there is a previous node then update it's next attribute
            # to refer to the next node of the node that is being removed.
            prev.next = curr.next
        else:
            # If there is no previous node then we are at the head of the list.
            # Update the first_node reference to the next node of the node 
            # that is being removed.
            self.first_node = curr.next
        # Delete the node that has been delinked.
        del curr

    def reverse_iterative(self):
        """ Returns a new LinkedList with the Nodes in reverse order. 

        This method uses an iterative approach.
        """
        # Create the new LinkedList.
        new_list = LinkedList()

        # Set the initial node to reverse from.
        node = self.first_node

        # iterate over each node and stop when node is None
        while node:
            next = node.next
            # Prepend the node to the new list.
            new_list.prepend(node)

            # Update the node reference.
            node = next
        return new_list

    def reverse_recursive(self, node=None, new_list=None):
        """ Returns a new LinkedList with the Nodes in reverse order. 

        This method uses a recursive approach.
        """
        if new_list is None:
            # First time through we initalise the new LinkedList
            # and set the initial node to being reversing from.
            new_list = LinkedList()
            if node is None:
                node = self.first_node

        if node:
            # If we have a node then prepend it to the new list.
            # As all nodes are being prepended the new list will
            # have the nodes in the reverse order. 
            next = node.next
            new_list.prepend(node)
            if next is not None:
                # If there are more nodes call this method again.
                self.reverse_recursive(next, new_list)

        # Node reference is None, so we've reached the end of
        # the LinkedList.
        return new_list

    def as_list(self):
        """ Returns this LinkedList as a `list` of Nodes. """
        nodes = []
        node = self.first_node
        while node:
            nodes.append(node)
            node = node.next
        return nodes

    def __len__(self):
        """ Returns the length/size of this LinkedList. """
        return len(self.as_list())

    def __str__(self):
        """ The string representation of the LinkedList. """
        return "->".join([str(n.data) for n in self.as_list()])
