from bits_handler.bit_operations import add
from bitarray import bitarray
import unittest


class PackageTest(unittest.TestCase):
    def test_add(self):
        res = bitarray('0000')
        a = '1000'
        b = '0100'
        self.assertEqual(res, add(a, b))
