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
import locale

try:
    import goslate
except ImportError:
    raise TypeError(u"Requer a lib goslate. \n\nUse:\n$ pip install goslate")


class Docgo(object):
    """ Translates docstrings by using Google Translator.

        :param obj: it's a python object with docstring that will inspected. An
                    error will raised (AssertionError) if not found docstring.
        :param lang: the target language. By default is used language from system.
        :return: translated text.

    """

    def __init__(self, obj, lang=None):
        self.language, self.encoding = self._get_locale()
        lang = lang if lang else self.language
        return self._help(obj, lang)

    def _get_locale(self):
        lang, encoding = locale.getdefaultlocale()
        return lang, encoding

    def _help(self, obj, lang):
        """ This is similar the bult-in function help but prints translated text.

        :param obj: class, module, function or any python object with docstring.
        """
        gs = goslate.Goslate()
        doc = inspect.getdoc(obj)
        doc_translated = gs.translate(doc, lang)
        print doc_translated.encode(self.encoding)
