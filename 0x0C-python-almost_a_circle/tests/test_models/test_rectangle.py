#!/usr/bin/python3
"""Module for rectangle module test"""

import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Test class for Base class"""

    def setUp(self):
        """General test variable"""

        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 8, 0, 12)
        r4 = Rectangle(10, "2", 0.0, 0.0, 12.0)
        r5 = Rectangle(10, 0, -3, -8, -12)

    def test_rectangle(self):
        """test method for Rectangle class"""

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r2.height, 10)

        with self.assertRaises(TypeError):
            r4.width
            r4.height
            r4.x
            r4.y

        with self.assertRaises(ValueError):
            r5.width
            r5.height
            r5.x
            r5.y

    def test_area(self):
        """test for area method"""

        self.assertEqual(r1.area(), 20)
        self.assertEqual(r3.area(), 16)

        with self.assertRaises(TypeError):
            r4.area()

        with self.assertEqual(ValueError):
            r5.area()


if __name__ == "__main__":
    unittest.main()
