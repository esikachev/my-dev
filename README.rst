

My-dev
======
.. image:: https://travis-ci.org/esikachev/my-dev-client.svg?branch=master
    :target: https://travis-ci.org/esikachev/my-dev-client

.. image:: https://coveralls.io/repos/esikachev/my-dev-client/badge.svg
    :target: https://coveralls.io/r/esikachev/my-dev-client


My-dev information
------------------

This is a utility for developers.

Preparing
---------

You need to install `sshpass` in your system.

For macos: ``brew install https://raw.githubusercontent.com/kadwanev/bigboybrew/master/Library/Formula/sshpass.rb``

For ubuntu: ``apt-get install sshpass``


Installation
------------

1. Clone project.

2. Install project. You have 2 ways:
   
2.1 Install in system

.. sourcecode:: console
   
    $ cd my-dev-client/
    $ sudo pip install .
..

2.2 Install in virtualenv    

.. sourcecode:: console

    $ tox -e venv --notest
..


How to use
----------

1. Init your account

.. sourcecode:: console

    $ my --init
..

2. Try to connect to any host in format:

.. sourcecode:: console
   
    $ my ssh host_user@host
..

3. Use ``my`` for connecting to host in the future:

.. sourcecode:: console
   
    $ my ssh host_user@host
..

Contacts
--------

You can contact us via mailing list: ``my-dev@googlegroups.com``
