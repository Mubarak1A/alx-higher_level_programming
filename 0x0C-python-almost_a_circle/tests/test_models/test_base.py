#!/usr/bin/python3
"""Module for base module test"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test class for Base class"""

    def test_base(self):
        """test method for Base class"""

        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base(4)
        b6 = Base(-5)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)
        self.assertEqual(b6.id, -5)
