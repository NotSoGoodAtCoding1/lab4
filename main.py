import unittest
from app import form


class TestForm(unittest.TestCase):

    def test_no_root(self):
        res = form(10, 0, 2)
        self.assertEqual(res, 'err')

    def test_single_root(self):
        res = form(10, 0, 0)
        self.assertEqual(len(res), 1)
        self.assertEqual(res, [0])

    def test_multiple_root(self):
        res = form(2, 5, -3)
        self.assertEqual(len(res), 2)
        self.assertEqual(res, [0.5, -3.0])


if __name__ == '__main__':
    unittest.main()