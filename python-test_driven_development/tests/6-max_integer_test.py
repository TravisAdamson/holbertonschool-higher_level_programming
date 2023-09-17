#!/usr/bin/python3
# 6-max_integer_test.py
# Travis Adamson
""" Unittests for function max_integer([..]). """


import unittest
max_integer = __import__('6-max_integer').max_integer


class Max_Integer_Test(unittest.Testcase)::
    """Define unittests for max_integer([..])."""

    def unsorted_list_test(self):
        """Tests against an unsorted list"""
        unsorted_list = [4, 2, 3, 5]
        self.assetEqual(max_integer(unsorted_list), 5)

    def sorted_list_test(self):
        """Tests against a sorted list"""
        sorted_list = [4, 5, 6, 7]
        self.assetEqual(max_integer(sorted_list), 7)

    def start_with_max_test(self):
        """Tests against a list starting with max"""
        start_with_max = [8, 5, 3, 1]
        self.assertEqual(max_integer(start_with_max), 8)

    def empty_list_test(self):
        """Tests against an empty list"""
        empty_list = []
        self.assertEqual(max_integer(empty), None)

    def single_element_list_test(self):
        """Tests against a list with a single element"""
        single_element = [10]
        self.assertEqual(max_integer(single_element), 10)

    def floating_test(self):
        """Tests against a list of floats"""
        floating_list = [2.8, 1.4, 80.1, 6.0]
        self.assertEqual(max_integer(floating_list), 80.1)

    def ints_and_floats_test(self):
        """Tests a list with int and float values"""
        int_and_float = [1, 8, 5.2, 15.3]
        self.assertEqual(max_integer(int_and_float), 15.3)

    def string_val_test(self):
        """Test against a string value"""
        string_val = "Travis"
        self.assertEqual(max_integer(string_val), 'v')

    def string_list_test(self):
        """Tests against a list of strings"""
        string_list = ["Travis", "typed", "this"]
        self.assertEqual(max_integer(string_list), "this")

    def empty_string_test(self):
        """Tests against an empty string"""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
