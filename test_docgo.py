#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Horacio Ibrahim'
__date__ = '2015-01-25'

''' Unit test for godoc module
'''

import unittest
import sys
import cStringIO
from docgo import *


class GodocTest(unittest.TestCase):

    def setUp(self):
        self.encoding = sys.getfilesystemencoding()

    def test_hp(self):
        stdout_ = sys.stdout # catch previous
        stream = cStringIO.StringIO()
        sys.stdout = stream
        dhelp(filter)
        sys.stdout = stdout_
        text_translated_pt_br = stream.getvalue()
        expected = text_translated_pt_br.startswith('filtro')
        self.assertTrue(expected)


if __name__ == '__main__':
    unittest.main()
