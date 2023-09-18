#!/usr/bin/python3
# 6-max_integer_test.py
# Travis Adamson
""" Unittests for function max_integer([..]). """


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_unsorted_list(self):
        """Tests against an unsorted list"""
        unsorted_list = [4, 2, 3, 5]
        self.assertEqual(max_integer(unsorted_list), 5)

    def test_sorted_list(self):
        """Tests against a sorted list"""
        sorted_list = [4, 5, 6, 7]
        self.assertEqual(max_integer(sorted_list), 7)

    def test_start_with_max(self):
        """Tests against a list starting with max"""
        start_with_max = [8, 5, 3, 1]
        self.assertEqual(max_integer(start_with_max), 8)

    def test_empty_list(self):
        """Tests against an empty list"""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_single_element_list(self):
        """Tests against a list with a single element"""
        single_element = [10]
        self.assertEqual(max_integer(single_element), 10)

    def test_floating(self):
        """Tests against a list of floats"""
        floating_list = [2.8, 1.4, 80.1, 6.0]
        self.assertEqual(max_integer(floating_list), 80.1)

    def test_ints_and_floats(self):
        """Tests a list with int and float values"""
        int_and_float = [1, 8, 5.2, 15.3]
        self.assertEqual(max_integer(int_and_float), 15.3)

    def test_string_val(self):
        """Test against a string value"""
        string_val = "Travis"
        self.assertEqual(max_integer(string_val), 'v')

    def test_string_list(self):
        """Tests against a list of strings"""
        string_list = ["Travis", "typed", "this"]
        self.assertEqual(max_integer(string_list), "typed")

    def test_empty_string(self):
        """Tests against an empty string"""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
