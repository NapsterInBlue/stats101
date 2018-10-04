=========
stats 101
=========

.. image:: https://img.shields.io/pypi/v/stats101.svg
        :target: https://pypi.python.org/pypi/stats101

.. image:: https://img.shields.io/travis/NapsterInBlue/stats101.svg
        :target: https://travis-ci.org/NapsterInBlue/stats101


Making doing super-basic statistics as trivial as it should be

Features
--------

* Confidence Intervals for sample means and proportions
* Literally nothing else yet!

Getting Started
---------------

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Installing
~~~~~~~~~~

A step by step series of examples that tell you how to get development environment running

Say what the step will be

.. code:: none

   pip install stats101 



Simple Demo
~~~~~~~~~~~

The following will return the 90% confidence interval for a given sample of a bunch of 0's and 1's

.. code:: python

   >>> import numpy as np
   >>> from stats101 import confidence_interval
   >>> X = np.random.randint(0, 2, (1000))
   >>> confidence_interval.proportion(0.90, X)
   
   (0.48198289796420185, 0.53401710203579811)


Project Goals
-------------

Tbh, I'll be surprised if I add much more to this beyond confidence intervals, but it can't hurt to leave this section, yeah?

Contributing
------------

For now, message me on twitter @NapsterInBlue if you wanna expand on this.

Running the tests
~~~~~~~~~~~~~~~~~

For the time being, you can run all unit tests with

.. code:: none

   pytest



Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template and egged on by judy2k_ on Twitter, lol

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _judy2k: https://twitter.com/judy2k/status/1047580226245578752

Also, it goes without saying that all of the actual hard work was originally done by the hard-working folks involved with `NumFocus <https://numfocus.org/sponsored-projects?_sft_project_category=python-interface>`_ and `SciPy <https://www.scipy.org/>`_
