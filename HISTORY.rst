.. :changelog:

History
-------

0.4.4 (2017-04-13)
~~~~~~~~~~~~~~~~~~

* Notify users for file i/o issues. Thanks @lukehinds!


0.4.3 (2017-04-13)
~~~~~~~~~~~~~~~~~~

* Restricted chardet to anything 3.0.2 or higher due to https://github.com/chardet/chardet/issues/113. Thanks @dan-blanchard for the quick fix!

0.4.2 (2017-04-12)
~~~~~~~~~~~~~~~~~~

* Restricted chardet to anything under 3.0 due to https://github.com/chardet/chardet/issues/113
* Added pyup badge
* Added utilities for pushing new versions up

0.4.0 (2015-08-21)
~~~~~~~~~~~~~~~~~~

* Enhanced detection for some binary streams and UTF texts. (#10, 11) Thanks `@pombredanne`_.
* Set up Appveyor for continuous testing on Windows. Thanks `@pydanny`_.
* Update link to Perl source implementation. (#9) Thanks `@asmeurer`_ `@pombredanne`_ `@audreyr`_.
* Handle UnicodeDecodeError in check. (#12) Thanks `@DRMacIver`_.
* Add very simple Hypothesis based tests. (#13) Thanks `@DRMacIver`_.
* Use setup to determine requirements and remove redundant requirements.txt. (#14) Thanks `@hackebrot`_.
* Add documentation status badge to README.rst. (#15) Thanks `@hackebrot`_.
* Run tox in travis.yml. Add pypy and Python 3.4 to tox environments. (#16) Thanks `@hackebrot`_ `@pydanny`_.
* Handle LookupError when detecting encoding. (#17) Thanks `@DRMacIver`_.


.. _`@pombredanne`: https://github.com/pombredanne
.. _`@pydanny`: https://github.com/pydanny
.. _`@asmeurer`: https://github.com/asmeurer
.. _`@audreyr`: https://github.com/audreyr
.. _`@DRMacIver`: https://github.com/DRMacIver
.. _`@hackebrot`: https://github.com/hackebrot

0.3.0 (2014-05-05)
~~~~~~~~~~~~~~~~~~

* Include tests, docs in source package. (#6) Thanks `@vincentbernat`_.
* Drop unnecessary shebangs and executable bits. (#8) Thanks `@scop`_.
* Generate string of printable extended ASCII bytes only once. (#7) Thanks `@scop`_.
* Make number of bytes to read parametrizable. (#7) Thanks `@scop`_.

.. _`@vincentbernat`: https://github.com/vincentbernat
.. _`@scop`: https://github.com/scop

0.2.0 (2013-09-22)
~~~~~~~~~~~~~~~~~~

* Complete rewrite of everything. Thanks `@ncoghlan`_.

.. _`@ncoghlan`: https://github.com/ncoghlan

0.1.1 (2013-08-17)
~~~~~~~~~~~~~~~~~~

* Tests pass under Python 2.6, 2.7, 3.3, PyPy.


0.1.0 (2013-08-17)
~~~~~~~~~~~~~~~~~~

* First release on PyPI.
