==========
Quickstart
==========

To use BinaryOrNot in a project, import it and use `is_binary()` to guess
whether a file is binary or text.

For example::

    >>> from binaryornot.check import is_binary
    >>> is_binary('README.rst')
    False

*****************
CommandLine Help
*****************

You can make use of BinaryOrNot on the commandline by using the `binaryornot` command
followed by your filename

For example::

    >>> binaryornot README.rst
    False

Please note, the `binaryornot` command requires one positional argument which is the filename
or `--help` to view the help function

For example::

    >>> binaryornot --help
