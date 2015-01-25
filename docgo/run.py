# -*- coding: UTF-8 -*-#
#
# Isto tradutor de pydoc's para ajudar iniciantes em python que não são
# fluentes em inglês. Lembre-se você precisará ser fluente para ser um exímio
# desenvolvedor python. But #babysteps is important!
#
# Este pacote usa o goslate de https://pypi.python.org/pypi/goslate
# LEMBRE: que o Google Tradutor faz traduções literais que
# podem não fazer sentido. Assim, às vezes, você precisará compensar isto.
#
# Uso:
# >>> from docgo import help as hp
# >>> hp(dir)
# dir ([objeto]) -> lista de strings
#     Se chamado sem argumentos, retorna os nomes no escopo atual.
#     Caso contrário, retornar uma lista em ordem alfabética de nomes que
#     compreende (alguns de) os atributos do objeto dado, e de atributos
#     alcançáveis a partir dele.
#     ... (conteúdo omitido)
#

import inspect
import sys

try:
    import goslate
except ImportError:
    raise TypeError(u"Requer a lib goslate. \n\nUse:\n$ pip install goslate")

def help(obj, lang='pt-br'):
    """ Prints translated text.

    :param obj: class, module, function or any python object with docstring.
    """
    encoding = sys.getfilesystemencoding()
    gs = goslate.Goslate()
    doc = inspect.getdoc(obj)
    doc_translated = gs.translate(doc, lang)
    print doc_translated.encode(encoding)
