.. amzlist documentation master file, created by
   sphinx-quickstart on Thu Apr 26 21:39:32 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

amzlist
=======

A linked list implementation by John Keyes.

.. toctree::
    :hidden:

    api/modules

Getting the code
----------------

The simplest way is to clone `the repository <https://github.com/jkeyes/amzlist>`_ from GitHub:

::

    git clone https://github.com/jkeyes/amzlist.git

Or you can download the repository in a `ZIP file <https://github.com/jkeyes/amzlist/zipball/master>`_.

Basic Usage
-----------

You can prepend items to a linked list, which adds each new Node as
the head of the list:

::

    from amzlist import LinkedList

    lnkd_list = LinkedList()
    lnkd_list.prepend("amazon.com")
    lnkd_list.prepend("@")
    lnkd_list.prepend("jkeyes")

You can also append. Note this is much slower as we must traverse the
entire list to find where to insert the node:

::

    lnkd_list.append("Why would you use append?")

It's also possible to insert a node after another node:

::

    from amzlist import Node
    n_color = Node("Red")
    n_answer = Node(42)

    lnkd_list.prepend(n_color)
    lnkd_list.insert(n_answer, n_color) # insert n_answer after n_color

To remove a node the `remove` method can be used:

::

    lnkd_list.remove("Red")

Alternatively you can use `push` and `pop` to add and remove
nodes from the list:

::

    lnkd_list.push("Item 1")
    lnkd_list.push("Item 2")
    node = lnkd_list.pop()
    node.data == "Item 2"

Reversing
---------

There are two methods to reverse the list, one uses an iterative
approach and the other a recursive one:

::

    rvsd_list = lnkd_list.reverse_iterative()
    rvsd_list = lnkd_list.reverse_recursive()

Cycle Detection
---------------
If the `LinkedList` methods are used no cycles can be introduced.
However, it is possible to introduct a cycle by directly 
manipulating the nodes:

::

    lnkd_list = LinkedList()
    node_john = Node('John')
    lnkd_list.prepend(node_john)
    node_james = Node('James')
    lnkd_list.prepend(node_james)
    node_joe = Node('Joe')
    lnkd_list.prepend(node_joe)
    
    # introduce a cycle
    # Joe->James->John->Jules->John
    node_jules = Node('Jules')
    node_john.next = node_jules
    node_jules.next = node_john

To prevent this you can create a `strict` LinkedList.

::

    lnkd_list = LinkedList(strict=True)
    ...
    node_jules.next = node_john
    # Raises ValueError

WARNING: this is an EXTREMELY costly feature, as it requires traversal
of the list for each Node that is added to the List (if the 
node being added has a value for `next`).

Running the Tests
-----------------
To run the testsuite you'll need to setup the environment first:

::

    cd amzlist
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

Then you can run the testsuite:

::

    nosetests tests

You can also get a coverage report:

::

    nosetests tests --with-coverage --cover-package amzlist

Continuous Integration
----------------------
The testsuite has been run on Python 2.5, 2.6, 2.7 and 3.2 on
`Travis CI <http://travis-ci.org/#!/jkeyes/amzlist>`_.

API Documentation
-----------------

Browse the `API Documentation <api/amzlist.html>`_. 

If you want to generate the documentation use the following 
commands:

::

    cd docs
    make html # docs will be generated in _build/html
