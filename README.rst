=============================
BinaryOrNot
=============================

.. image:: https://badge.fury.io/py/binaryornot.png
    :target: http://badge.fury.io/py/binaryornot
    
.. image:: https://travis-ci.org/audreyr/binaryornot.png?branch=master
        :target: https://travis-ci.org/audreyr/binaryornot

.. image:: https://pypip.in/d/binaryornot/badge.png
        :target: https://crate.io/packages/binaryornot?version=latest


Ultra-lightweight pure Python package to check if a file is binary or text.

* Free software: BSD license
* Documentation: http://binaryornot.readthedocs.org

Status
------

It works, and I'm using this package in various places.

The code could be improved. Pull requests welcome! As of now, it is based on
these snippets, but that may change:

* http://stackoverflow.com/questions/898669/how-can-i-detect-if-a-file-is-binary-non-text-in-python
* http://stackoverflow.com/questions/1446549/how-to-identify-binary-and-text-files-using-python
* http://code.activestate.com/recipes/173220/


Features
--------

Has tests for these file types:

* Text: .css, .json, .txt, .svg
* Binary: .eot, .otf, ttf, .woff, .png, .jpg, .tiff, .bmp

Why?
----

You may be thinking, "I can write this in 2 lines of code?!"

Sure, but this package saves you from having to write and thoroughly test
those 2 lines of code with all sorts of weird file types, cross-platform.
