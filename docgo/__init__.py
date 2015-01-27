"""
docgo is a translator lib to docstring that uses Google Tradutor (online).

Usage
=====
import docgo
docgo.dhelp(filter) # the default language retrieved from system
...
docgo.dhelp(dir, lang='en') # you can pass optional language
...

"""

# RELEASES 0.6
# + Fix typo in setup.py from godoc to docgo

# RELEASES 0.5
# + Added support for multiple language
# + Automatically get language from system [optional, default is pt-br]
# + Added >>dhelp<< attribute for do analogy the built-in help function
# + Changed README.md to support new dhelp approach

# ROADMAP
# + Display side by side original and translated texts
# + To improve formatted text to take more near original
# + Not translate object, bulit-in, statements name e.g filter to filtro
#   (in case portuguese)
# +

from run import *

dhelp = Docgo
