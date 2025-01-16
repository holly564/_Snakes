import unittest
from utils import to_str


class UtilsErrorTestCase(unittest.TestCase):
    def test_to_str_bad(self):
        with self.assertRaises(TypeError):
            to_str(object())

    def test_to_bad_encoding(self):
        with self.assertRaises(UnicodeDecodeError):
            to_str(b"\xfa\xfa")

if __name__ == '__main__':
    unittest.main()
