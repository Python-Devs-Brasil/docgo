docgo: a small tradutor for python's docstring
===============================================

``docgo`` uses goslate to make translations of Python's Docstring.
See goslate for more details.

Usage
=====
```
>>> from docgo import *
>>> dhelp(dir) # the default language retrieved from system
 dir ([objeto]) -> lista de strings
 ...
# or
>>> dhelp(dir, lang='en') # you can pass optional language
 ...
 ```

Install
=======

 ```
 $ pip install docgo
 ```
