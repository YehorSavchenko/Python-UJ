import math
import unittest

from Zestaw6.points import Point


class Circle:
    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("Negative radius")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return f'Circle({self.pt.x}, {self.pt.y}, {self.radius})'

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return math.pi * math.pow(self.radius, 2)

    def move(self, x, y):
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)

    def cover(self, other):
        x_center = (self.pt.x + other.pt.x) / 2
        y_center = (self.pt.y + other.pt.y) / 2

        radius1 = math.sqrt(pow(x_center - self.pt.x, 2) + pow(y_center - self.pt.y, 2)) + self.radius
        radius2 = math.sqrt(pow(x_center - other.pt.x, 2) + pow(y_center - other.pt.y, 2)) + other.radius
        radius = max(radius1, radius2)

        return Circle(x_center, y_center, radius)


class TestCircle(unittest.TestCase):
    def setUp(self): pass

    def test_cmp(self):
        self.assertTrue(Circle(3, 3, 5) != Circle(3, 3, 6))
        self.assertTrue(Circle(6, 6, 2) != Circle(2, 1, 9))
        self.assertFalse(Circle(1, 1, 5) != Circle(1, 1, 5))
        self.assertTrue(Circle(3, 3, 5) == Circle(3, 3, 5))
        self.assertFalse(Circle(3, 3, 5) == Circle(1, 3, 3))

    def test_print(self):
        self.assertEqual("Circle(3, 2, 3)", Circle(3, 2, 3).__repr__())
        self.assertEqual("Circle(6, 2, 3)", Circle(6, 2, 3).__repr__())

    def test_area(self):
        self.assertEqual(Circle(1, 1, 2).area(), 4 * math.pi)
        self.assertEqual(Circle(1, 2, 3).area(), 9 * math.pi)

    def test_move(self):
        self.assertEqual(Circle(1, 2, 3).move(1, 2), Circle(2, 4, 3))
        self.assertEqual(Circle(4, 5, 6).move(7, 8), Circle(11, 13, 6))

    def test_cover(self):
        self.assertEqual(Circle(0, 0, 2).cover(Circle(0, 2, 2)), Circle(0, 1, 3))
        self.assertEqual(Circle(0, 0, 1).cover(Circle(0, 0, 2)), Circle(0, 0, 2))

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
