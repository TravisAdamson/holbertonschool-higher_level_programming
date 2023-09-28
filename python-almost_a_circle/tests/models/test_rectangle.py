#!/usr/bin/python3
# test_rectangle.py
# Travis Adamson
"""Describes the unittests for rectangle.py file"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Unittests that test instantiation of the new class: Rectangle"""

    def test_rectangle_is_also_base(self):
        self.assertIsInstance(Rectangle(15, 20), Base)

    def test_no_argument(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_argument(self):
        with self.assertRaises(TypeError):
            Rectangle(10)

    def test_two_arguments(self):
        rect1 = Rectangle(15, 10)
        rect2 = Rectangle(20, 15)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_three(self):
        rect1 = Rectangle(15, 20, 0)
        rect2 = Rectangle(20, 15, 5)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_four(self):
        rect1 = Rectangle(15, 20, 0, 0)
        rect2 = Rectangle(20, 15, 5, 5)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_with_five(self):
        self.assertEqual(15, Rectangle(15, 20, 0, 0, 15).id)

    def test_too_many_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 6, 1, 2, 3, 10)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(12, 20, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(12, 20, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(12, 20, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(12, 20, 0, 0, 1).__y)

    def test_width_getter(self):
        r = Rectangle(15, 17, 17, 15, 11)
        self.assertEqual(15, r.width)

    def test_height_getter(self):
        r = Rectangle(15, 17, 17, 15, 11)
        self.assertEqual(17, r.height)

    def test_x_getter(self):
        r = Rectangle(15, 17, 17, 15, 11)
        self.assertEqual(17, r.x)

    def test_y_getter(self):
        r = Rectangle(15, 17, 17, 15, 11)
        self.assertEqual(15, r.y)

    def test_width_setter(self):
        r = Rectangle(15, 17, 17, 15, 11)
        r.width = 8
        self.assertEqual(8, r.width)

    def test_height_setter(self):
        r = Rectangle(15, 17, 17, 15, 11)
        r.height = 8
        self.assertEqual(8, r.height)

    def test_x_setter(self):
        r = Rectangle(15, 17, 17, 15, 11)
        r.x = 8
        self.assertEqual(8, r.x)

    def test_y_setter(self):
        r = Rectangle(15, 17, 17, 15, 11)
        r.y = 8
        self.assertEqual(8, r.y)


class TestRectangle_width(unittest.TestCase):
    """Unittests for intialization of Rectangles width"""

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 20)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("bad", 20)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 5)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 20)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"first": 10, "second": 20}, 20)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([10, 20, 30], 20)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({10, 20, 30}, 20)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((10, 20), 20)

    def test_frozenset_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({10, 20, 30, 10}), 20)

    def test_range_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(3), 20)

    def test_bytes_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Python', 20)

    def test_bytearray_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'abcd'), 20)

    def test_momoryview_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'abcd'), 20)

    def test_inf_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 20)

    def test_nan_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 20)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 20)

    def test_zero_width(self):
        with self.assertRaiseRegex(ValueError, "width must be > 0"):
            Rectangle(0, 20)


class TestRectangle_height(unittest.TestCase):
    """Unittests for intialization of Rectangles height"""

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 20)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "bad")

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, 5.5)

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, complex(5))

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(20, {"first": 10, "second": 20})

    def test_bool_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, True)

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(20, [10, 20, 30])

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(20, {10, 20, 30})

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(20, (10, 20))

    def test_frozenset_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, frozenset({10, 20, 30, 10}))

    def test_range_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, range(3))

    def test_bytes_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, b'Python')

    def test_bytearray_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, bytearray(b'abcd'))

    def test_momoryview_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, memoryview(b'abcd'))

    def test_inf_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, float('inf'))

    def test_nan_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, float('nan'))

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -20)

    def test_zero_height(self):
        with self.assertRaiseRegex(ValueError, "height must be > 0"):
            Rectangle(20, 0)


class TestRectangle_x(unittest.TestCase):
    """Unittests for intialization of Rectangles x value"""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, "NONE")

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, "bad")

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, "5.5")

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, complex(5))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, {"first": 10, "second": 20})

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, True)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, [10, 20])

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, {10, 20})

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, (10, 20))

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, frozenset({10, 20}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, range(5))

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, b'Python')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, bytearray(b'abcd'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, memoryview(b'abcd'))

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, float('inf'))

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, float('nan'))

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 20, -20)


class TestRectangle_y(unittest.TestCase):
    """Unittests for intialization of Rectangles y value"""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, "NONE")

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, "bad")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, "5.5")

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, {"first": 10, "second": 20})

    def test_bool_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, True)

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, [10, 20])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, {10, 20})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, (10, 20))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, frozenset({10, 20}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, b'Python')

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, bytearray(b'abcd'))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, memoryview(b'abcd'))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, float('nan'))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 20, 1, -5)


class TestRectangle_order(unittest.TestCase):
    """Unittests for testing Rectangle order of attribute initialization."""

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("inv width", "inv height")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("inv width", 2, "inv x")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("inv width", 2, 3, "inv y")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "inv height", "inv x")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "inv height", 2, "inv y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "inv x", "inv y")


class TestRectangle_area(unittest.TestCase):
    """Unittests for testing Rectangles area method"""

    def test_area_smaller(self):
        rect1 = Rectangle(20, 3, 0, 0, 0)
        self.assertEqual(60, rect1.area())

    def test_area_larger(self):
        rect1 = Rectangle(1000000000, 3, 0, 0, 0)
        self.assertEqual(3000000000, rect1.area())

    def test_area_changed_values(self):
        rect1 = Rectangle(20, 10, 0, 0, 0)
        rect1.width = 10
        rect1.height = 5
        self.assertEqual(50, rect1.area())

    def test_area_with_arg(self):
        rect1 = Rectangle(10, 10, 0, 0, 0)
        with self.assertRaises(TypeError):
            rect1.area(10)
