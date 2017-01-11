My-dev
========
.. image:: https://travis-ci.org/esikachev/my-dev.svg?branch=master
    :target: https://travis-ci.org/esikachev/my-dev


**My-dev information**

This is a utility for developers.


**Installation**

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

3. Create a config-file in home-directory or in project-directory ``.my.conf``
   with host and username. Example of config-file you can found in ``etc/my_dev/.my.conf.sample``.

3. Try to use MY. For example:

.. sourcecode:: console

    $ my ssh controller
..


**How to use**

1. Init your account

.. sourcecode:: console
   
    $ my init
..
