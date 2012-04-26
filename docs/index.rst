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

The simplest way is to clone the repository:

::

    git clone https://github.com/jkeyes/amzlist.git

Or you can download the repository in a `ZIP file <https://github.com/jkeyes/amzlist/zipball/master>`_.

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
