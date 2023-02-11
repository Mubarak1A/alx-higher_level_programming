#!/usr/bin/python3
"""Module for rectangle module test"""

import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Test class for Base class"""

    def test_rectangle(self):
        """test method for Rectangle class"""

        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r2.height, 10)


if __name__ == "__main__":
    unittest.main()
