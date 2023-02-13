#!/usr/bin/python3
"""Module for square module test"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test class for Rectangle class"""

    def setUp(self):
        """General test variable"""
        r1 = Square(10)
        r2 = Square(2)
        r3 = Square(10, 0, 0, 12)
        r4 = Square(10.0, 0.0, 0.0, 12)
        r5 = Square(-8, -3, -8, 12)

    def test_rectangle(self):
        """test method for Square class"""
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r1.size, 10)
        self.assertEqual(r2.height, 2)

        with self.assertRaises(TypeError):
            r4.width
            r4.height
            r4.x
            r4.y
