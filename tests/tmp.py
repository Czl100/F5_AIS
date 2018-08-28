#_*_ coding: utf-8 _*_
import unittest
import sys
import os
import struct
import StringIO
import logging

from PIL import Image
import jpype
import optparse

tests_dir = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(tests_dir, '..'))

import jpeg_encoder
from jpeg_encoder import JpegInfo, JpegEncoder
from test_util import JavaF5Random
from test_util import F5TestCase
from huffman import Huffman

class JpegInfoTest(F5TestCase):
    def test_init(self):
        print('Class:JpegInfoTest(F5TestCase)_test_init()')

class HuffmanTest(F5TestCase):
    def test_init(self):
        print('class:HuffmanTest_test_init')        #1

        def check(py, ja):
            print(str(py),str(ja))
                        
        check('check1', 'jaac')                     #2
        check('check2', 'jaac')                     #3

class JpegEncoderTest(F5TestCase):
    def _test_compress(self, embed_data):
        print(embed_data)

    def test_compress_no_embedded_data(self):
        self._test_compress(None)

    def test_compress_with_short_embedded_data(self):
        self._test_compress('i')

    def test_compress_with_long_embedded_data(self):
        self._test_compress('test eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeembed\n')
        
    def test_compress_with_chinese_embedded_data(self):
        self._test_compress('我的测试用例')

if __name__ == '__main__':
    unittest.main()

