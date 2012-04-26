.. amzlist documentation master file, created by
   sphinx-quickstart on Thu Apr 26 21:39:32 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

amzlist
=======

A linked list implementation by John Keyes.

.. toctree::

   api/modules

To run the testsuite you'll need to setup the environment first:

::

    cd amzlist
    virtualenv venv
    pip install -r requirements.txt

Then you can run the testsuite:

::

    nosetests tests

You can also get a coverage report:

::

    nosetests tests --with-coverage --cover-package amzlist

