import unittest
from app import add, subtract, multiply, percentage

class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(1.5, 2.5), 4.0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(1.5, 0.5), 1.0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(1.5, 2), 3.0)

    def test_percentage(self):
        self.assertEqual(percentage(50, 100), 50.0)
        self.assertEqual(percentage(25, 50), 50.0)
        self.assertEqual(percentage(0, 100), 0.0)
        with self.assertRaises(ValueError):
            percentage(1, 0)

if __name__ == '__main__':
    unittest.main()