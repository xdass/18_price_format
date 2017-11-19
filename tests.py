import unittest
import format_price as fp


class PricetTest(unittest.TestCase):
    def test_simple_number(self):
        self.assertEquals(fp.format_price(76521), '76 521')

    def test_with_decimal_point(self):
        self.assertEquals(fp.format_price(3245.000000), '3 245')

    def test_decimal_point(self):
        self.assertEqual(fp.format_price(9999.999), '9 999.99')

    def test_str_price(self):
        self.assertEquals(fp.format_price('daassda'), None)

    def test_wrong_number(self):
        self.assertEquals(fp.format_price('123.123.123'), None)

    def test_negative_number(self):
        self.assertEqual(fp.format_price('-40000'), None)