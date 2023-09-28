#!/usr/bin/python3
# test_base.py
# Travis Adamson
"""Describes the unittests for base.py file"""
import unittest
from models.base import Base


class TestBase_instantiation(unittest.TestCase):
    """Unittests that test instantiation of the new class: Base"""

    def test_no_argument(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_now_there_are_three(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 2)

    def test_given_id(self):
        self.assertEqual(15, Base(15).id)

    def test_nb_value_after_given_id(self):
        base1 = Base()
        base2 = Base(15)
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 1)

    def test_is_id_public(self):
        base = Base(15)
        base.id = 20
        self.assertEqual(20, base.id)

    def test_is_nb_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)
