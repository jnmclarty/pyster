======
PySter
======
Python anywhere
---------------

Demo
====
Watch a demo, be sure to enable HD, on `Vimeo <https://vimeo.com/121615286>`_

Requirements & Mandatory Dependencies
=====================================
* Windows 7
* Python 2.7 32-bit
* rrsm - ``pip install rrsm``
* PyHook - See `SourceForge.net <http://sourceforge.net/projects/pyhook/>`_.
* PyWin32 - See `Gohlke's binaries <http://www.lfd.uci.edu/~gohlke/pythonlibs/#pywin32>`_.

Optional Dependencies
=====================
Just remove any reference to dataframes, if you don't have pandas.

* pandas - http://pandas.pydata.org

Installation & Use
==================
1. download & extract or clone or ``pip install pyster``
2. python engine.py
3. Type ">>>", some python, then press the right arrow key to "execute".
4. Optionally, edit pyster/pyster_extensions/functionality.py to suite, then re-run.

PSA
===
This software should only be sourced from places/formats which allow you to review the code.  It's recommended to 
only use this software on closed or low-priority systems.  PySter is basically a keylogger (without the logging/saving)
combined with all of the risks exposed by exec() and/or compile().

Known Issues & Bugs
===================
This software is barely beta level quality.  There are a variety of problems that need to be fixed, prior to an 
initial release of PySter.  

These are the known ones:

1. Certain rare exceptions thrown from exec(), and compile(), mainly of the TypeError variety, can cause PySter to enter an unhandled/unrecoverable/unresponsive state.
2. An issue associated with with memory usage, timing, or a bug in PyWin32, cause strange integer type errors at strange times.
3. The string representation of many objects often need PySter wrappers to display properly.  Eg. p2e().
4. Many forms of software mutilate the keyboard input;  these programs often won't work as expected with PySter. Eg. Spyder, for things like line breaks.

See the various branches of this repo for starts of attempts to handle 1 and 2.



