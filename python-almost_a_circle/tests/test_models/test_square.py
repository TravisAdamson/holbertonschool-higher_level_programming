#!/usr/bin/python3
# test_square.py
# Travis Adamson
"""Describes the unittests for square.py file

Unittest classes:
    TestSquare_instantiation - line
    TestSquare_size - line
    TestSquare_x - line
    TestSquare_y - line
    TestSquare_order - line
    TestSquare_area - line
    TestSquare_output - line
    TestSquare_update_args - line
    TestSquare_update_kwargs - line
    TestSquare_to_dictionary - line
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unittests that test instantiation of the new class: Square"""

    def test_square_is_also_base(self):
        self.assertIsInstance(Square(15), Base)

    def test_square_is_also_rectangle(self):
        self.assertIsInstance(Square(15), Rectangle)

    def test_no_argument(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_argument(self):
        sq1 = Square(10)
        sq2 = Square(15)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_two_arguments(self):
        sq1 = Square(15, 1)
        sq2 = Square(20, 1)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_three(self):
        sq1 = Square(15, 1, 0)
        sq2 = Square(20, 1, 5)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_four(self):
        self.assertEqual(15, Square(20, 15, 5, 15).id)

    def test_too_many_arguments(self):
        with self.assertRaises(TypeError):
            Square(5, 6, 1, 2, 3, 10)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(12, 20, 0, 1).__size)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Square(12, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Square(12, 20, 0, 1).__y)

    def test_size_getter(self):
        self.assertEqual(15, Square(15, 17, 17, 11).size)

    def test_width_getter(self):
        sq1 = Square(10, 5, 3, 1)
        sq1.size = 4
        self.assertEqual(4, sq1.width)

    def test_height_getter(self):
        sq1 = Square(10, 5, 3, 1)
        sq1.size = 4
        self.assertEqual(4, sq1.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(5).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(5).y)

    def test_size_setter(self):
        sq1 = Square(15, 17, 15, 11)
        sq1.size = 4
        self.assertEqual(4, sq1.size)


class TestSquare_size(unittest.TestCase):
    """Unittests for intialization of Squares size"""

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("bad")

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def test_complex_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(5))

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"first": 10, "second": 20})

    def test_bool_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([10, 20, 30])

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({10, 20, 30})

    def test_tuple_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((10, 20))

    def test_frozenset_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({10, 20, 30, 10}))

    def test_range_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(3))

    def test_bytes_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'Python')

    def test_bytearray_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'abcd'))

    def test_momoryview_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'abcd'))

    def test_inf_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_nan_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-10)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)


class TestSquare_x(unittest.TestCase):
    """Unittests for intialization of Square x value"""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, "bad")

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, 5.5)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, complex(5))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, {"first": 10, "second": 20})

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, True)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, [10, 20])

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, {10, 20})

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, (10, 20))

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, frozenset({10, 20}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, range(5))

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, b'Python')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, bytearray(b'abcd'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, memoryview(b'abcd'))

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, float('inf'))

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, float('nan'))

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(10, -20)


class TestSquare_y(unittest.TestCase):
    """Unittests for intialization of Square y value"""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, "bad")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, 5.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, {"first": 10, "second": 20})

    def test_bool_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, True)

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, [10, 20])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, {10, 20})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, (10, 20))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, frozenset({10, 20}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, b'Python')

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, bytearray(b'abcd'))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, memoryview(b'abcd'))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, float('nan'))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(10, 1, -5)


class TestSquare_order(unittest.TestCase):
    """Unittests for testing Square order of attribute initialization."""

    def test_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("inv size", "inv x")

    def test_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("inv size", 3, "inv y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "inv x", "inv y")


class TestSquare_area(unittest.TestCase):
    """Unittests for testing Square area"""

    def test_area_smaller(self):
        self.assertEqual(400, Square(20, 0, 0, 1).area())

    def test_area_larger(self):
        sq1 = Square(1000000000, 0, 0, 1)
        self.assertEqual(1000000000000000000, sq1.area())

    def test_area_changed_size(self):
        sq1 = Square(10, 0, 0, 1)
        sq1.size = 5
        self.assertEqual(25, sq1.area())

    def test_area_with_arg(self):
        sq1 = Square(10, 0, 0, 1)
        with self.assertRaises(TypeError):
            sq1.area(15)
