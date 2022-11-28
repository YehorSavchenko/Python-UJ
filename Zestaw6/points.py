import math
import unittest


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0:d},{1:d})".format(self.x, self.y)

    def __repr__(self):
        return "Point({0:d},{1:d})".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __hash__(self):
        return hash((self.x, self.y))


class TestTime(unittest.TestCase):
    def setUp(self):
        self.x = 0
        self.y = 0

    def testPrint(self):
        self.assertEqual(Point(2, 2).__repr__(), 'Point(2,2)')
        self.assertEqual(Point(-1, 0).__repr__(), 'Point(-1,0)')
        self.assertEqual(Point(0, 0).__repr__(), 'Point(0,0)')
        self.assertEqual(Point(3, 7).__str__(), '(3,7)')
        self.assertEqual(Point(-1, 5).__str__(), '(-1,5)')

    def test_cmp(self):
        self.assertTrue(Point(1, 1) == Point(1, 1))
        self.assertFalse(Point(1, 1) == Point(1, 2))
        self.assertFalse(Point(1, 1) != Point(1, 1))
        self.assertTrue(Point(1, 1) != Point(1, 2))

    def test_add(self):
        self.assertEqual(Point(1, 2) + Point(2, 3), Point(3, 5))
        self.assertEqual(Point(-1, -2) + Point(2, 3), Point(1, 1))
        self.assertEqual(Point(0, 0) + Point(2, 3), Point(2, 3))

    def test_sub(self):
        self.assertEqual(Point(1, 2) - Point(2, 3), Point(-1, -1))
        self.assertEqual(Point(-1, -2) - Point(2, 3), Point(-3, -5))
        self.assertEqual(Point(0, 0) - Point(2, 3), Point(-2, -3))

    def test_mul(self):
        self.assertEqual(Point(1, 2) * Point(2, 3), 8)
        self.assertEqual(Point(-1, -2) * Point(2, 3), -8)
        self.assertEqual(Point(0, 0) * Point(2, 3), 0)

    def test_cross(self):
        self.assertEqual(Point(-1, -2).cross(Point(1, 2)), 0)
        self.assertEqual(Point(1, 2).cross(Point(1, 2)), 0)

    def test_length(self):
        self.assertEqual(Point(16, 0).length(), 16)
        self.assertEqual(Point(2, 3).length(), math.sqrt(2 * 2 + 3 * 3))


if __name__ == "__main__":
    unittest.main()
