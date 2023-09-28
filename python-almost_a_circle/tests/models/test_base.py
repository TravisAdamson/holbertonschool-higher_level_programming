#!/usr/bin/python3
# test_base.py
# Travis Adamson
"""Describes the unittests for base.py file"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_str_id(self):
        self.assertEqual("Help", Base("Help").id)

    def test_float_id(self):
        self.assertEqual(2.2, Base(2.2).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual({"k": 10, "v": 20}, Base({"k": 10, "v": 20}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_tuple_id(self):
        self.assertEqual((10, 20), Base((10, 20)).id)

    def test_set_id(self):
        self.assertEqual({10, 20, 30}, Base({10, 20, 30}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(3), Base(range(3)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcd'), Base(bytearray(b'abcd')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcd'), Base(memoryview(b'abcd')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_nan_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_arguments(self):
        with self.assertRaises(TypeError):
            Base(10, 20)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method"""

    def test_to_json_string_rectangle_type(self):
        r1 = Rectangle(15, 5, 1, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([r1.to_dictionary()])))

    def test_to_json_string_rectangle_one_dicttionary(self):
        r1 = Rectangle(15, 5, 1, 3, 4)
        self.assertTrue(len(Base.to_json_string([r1.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dictionaries(self):
        r1 = Rectangle(15, 5, 1, 3, 4)
        r2 = Rectangle(10, 4, 2, 1, 3)
        list_dictionaries = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dictionaries)) == 106)

    def test_to_json_string_square_type(self):
        s1 = Square(15, 3, 1, 2)
        self.assertEqual(str, type(Base.to_json_string([s1.to_dictionary()])))

    def test_to_json_string_square_one_dictionary(self):
        s1 = Square(15, 3, 1, 2)
        self.assertTrue(len(Base.to_json_string([s1.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dictionaries(self):
        s1 = Square(15, 3, 1, 2)
        s2 = Square(10, 2, 3, 5)
        list_dictionaries = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dictionaries)) == 78)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_arguments(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_too_many_arguments(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 10)


class TestBase_from_json_string(unittest.TestCase):
    """Unittesting for the from_json_string method"""

    def test_from_json_string_type(self):
        list_in = [{"id": 18, "width": 2, "height": 2}]
        json_list_in = Rectangle.to_json_string(list_in)
        list_out = Rectangle.from_json_string(json_list_in)
        self.assertEqual(list, type(list_out))

    def test_from_json_string_one_rect(self):
        list_in = [{"id": 18, "width": 2, "height": 2, "x": 1}]
        json_list_in = Rectangle.to_json_string(list_in)
        list_out = Rectangle.from_json_string(json_list_in)
        self.assertEqual(list_in, list_out)

    def test_from_json_string_two_rect(self):
        list_in = [
            {"id": 10, "width": 2, "height": 2, "x": 1, "y": 1},
            {"id": 8, "width": 3, "height": 3, "x": 2, "y": 2},
        ]
        json_list_in = Rectangle.to_json_string(list_in)
        list_out = Rectangle.from_json_string(json_list_in)
        self.assertEqual(list_in, list_out)

    def test_from_json_string_one_square(self):
        list_in = [{"id": 10, "size": 2}]
        json_list_in = Square.to_json_string(list_in)
        list_out = Square.from_json_string(json_list_in)
        self.assertEqual(list_in, list_out)

    def test_from_json_string_two_square(self):
        list_in = [
            {"id": 10, "size": 3},
            {"id": 8, "size": 2},
        ]
        json_list_in = Square.to_json_string(list_in)
        list_out = Square.from_json_string(json_list_in)
        self.assertEqual(list_in, list_out)

    def test_from_json_string_none(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_arguments(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_too_many_arguments(self):
        with self.assertRaises(TypeError):
            Base.from_jason_string([], 10)
