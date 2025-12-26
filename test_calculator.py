import unittest
import math
from operations import *
from memory import *

class TestOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(5, 0), 'Ошибка') 

    def test_mod(self):
        self.assertEqual(mod(10, 3), 1)
        self.assertEqual(mod(10, 0), 'Ошибка') 

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)

    def test_sqrt_num(self):
        self.assertEqual(sqrt_num(9), 3)
        self.assertEqual(sqrt_num(-4), 'Ошибка')  

    def test_sin_deg(self):
        self.assertAlmostEqual(sin_deg(30), 0.5, places=5)

    def test_cos_deg(self):
        self.assertAlmostEqual(cos_deg(60), 0.5, places=5)

    def test_floor_num(self):
        self.assertEqual(floor_num(2.7), 2)
        self.assertEqual(floor_num(-2.3), -3)

    def test_ceil_num(self):
        self.assertEqual(ceil_num(2.1), 3)
        self.assertEqual(ceil_num(-2.7), -2)

class TestMemory(unittest.TestCase):

    def setUp(self):
        memory_clear()  

    def test_memory_add_and_recall(self):
        memory_add(5)
        self.assertEqual(memory_recall(), 5)
        memory_add(3)
        self.assertEqual(memory_recall(), 8)

    def test_memory_clear(self):
        memory_add(10)
        memory_clear()
        self.assertEqual(memory_recall(), 0)

if __name__ == '__main__':
    unittest.main()
