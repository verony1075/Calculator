import unittest
from calc import Calc

class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-2, 3), 1)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_sub(self):
        self.assertEqual(self.calc.sub(2, 3), -1)
        self.assertEqual(self.calc.sub(-2, 3), -5)
        self.assertEqual(self.calc.sub(0, 0), 0)

    def test_mul(self):
        self.assertEqual(self.calc.mul(2, 3), 6)
        self.assertEqual(self.calc.mul(-2, 3), -6)
        self.assertEqual(self.calc.mul(0, 5), 0)

    def test_div(self):
        self.assertEqual(self.calc.div(6, 3), 2)
        self.assertEqual(self.calc.div(-6, 3), -2)
        self.assertEqual(self.calc.div(0, 5), 0)
        with self.assertRaises(ZeroDivisionError):
            self.calc.div(5, 0)

    def test_pow(self):
        self.assertEqual(self.calc.pow(2, 3), 8)
        self.assertEqual(self.calc.pow(-2, 3), -8)
        self.assertEqual(self.calc.pow(0, 5), 0)
        self.assertEqual(self.calc.pow(1, 100), 1)

if __name__ == '__main__':
    unittest.main()