# PySter Beta
Python *anywhere

### Demo
##### To watch in HD, click through to Vimeo
[![PySter Beta Demo](https://i.vimeocdn.com/video/510032230.webp?mw=960&amp;mh=540)](https://vimeo.com/121615286)

### Requirements & Mandatory Dependencies

* Windows 7
* Python 2.7 32-bit
* PyHook - See [SourceForge.net](http://sourceforge.net/projects/pyhook/)
* PyWin32 - [See Gohlke's binaries](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pywin32)
* rrsm - ```pip install rrsm```

### Optional Dependencies

Just remove any reference to dataframes, if you don't have pandas.

* pandas - http://pandas.pydata.org

### Installation & Use

1. download & extract or clone
2. python engine.py
3. Type ">>>", some python, then press the right arrow key to "execute".
4. Optionally, edit [pyster/pyster_extensions/functionality.py](https://github.com/jnmclarty/pyster/blob/master/pyster/pyster_extensions/functionality.py) to suite, then re-run.

### License

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">PySter</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Jeffrey McLarty</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/jnmclarty/pyster" rel="dct:source">https://github.com/jnmclarty/pyster</a>.


### PSA

This software should only be sourced from places/formats which allow you to review the code.  It's recommended to 
only use this software on closed or low-priority systems.  PySter is basically a keylogger (without the logging/saving)
combined with all of the risks exposed by exec() and/or compile().

### Known issues & bugs

This software is barely beta level quality.  There are a variety of problems that need to be fixed, prior to an 
initial release of PySter.  

These are the known ones:

1. Certain rare exceptions thrown from exec(), and compile(), mainly of the TypeError variety, can cause PySter to enter an unhandled/unrecoverable/unresponsive state.
2. An issue associated with with memory usage, timing, or a bug in PyWin32, cause strange integer type errors at strange times.
3. The string representation of many objects often need PySter wrappers to display properly.  Eg. p2e().
4. Many forms of software mutilate the keyboard input;  these programs often won't work as expected with PySter. Eg. Spyder, for things like line breaks.

See the various branches of this repo for starts of attempts to handle 1 and 2.



