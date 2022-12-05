import math

import pytest

from Zestaw6.points import Point
from Zestaw8.circle import Circle


def test_cmp_equal():
    assert (Circle(3, 3, 5) != Circle(3, 3, 6))
    assert (Circle(6, 6, 2) != Circle(2, 1, 9))
    assert (Circle(1, 1, 5) == Circle(1, 1, 5))
    assert (Circle(3, 3, 5) == Circle(3, 3, 5))
    assert (Circle(3, 3, 5) != Circle(1, 3, 3))


def test_print():
    assert ("Circle(3, 2, 3)" == Circle(3, 2, 3).__repr__())
    assert ("Circle(6, 2, 3)" == Circle(6, 2, 3).__repr__())


def test_area():
    assert (Circle(1, 1, 2).area() == 4 * math.pi)
    assert (Circle(1, 2, 3).area() == 9 * math.pi)


def test_move():
    assert (Circle(1, 2, 3).move(1, 2) == Circle(2, 4, 3))
    assert (Circle(4, 5, 6).move(7, 8) == Circle(11, 13, 6))


def test_cover():
    assert (Circle(0, 0, 2).cover(Circle(0, 2, 2)) == Circle(0, 1, 3))
    assert (Circle(0, 0, 1).cover(Circle(0, 0, 2)) == Circle(0, 0, 2))


def test_from_point():
    assert (Circle.from_points((Point(1, 1), Point(2, 4), Point(5, 3))) == Circle(3, 2, 2.24))
    assert (Circle.from_points((Point(1, 0), Point(-1, 0), Point(0, 1))) == Circle(0, 0, 1))
    assert (Circle.from_points((Point(1, -6), Point(2, 1), Point(5, 2))) == Circle(5, -3, 5))


if __name__ == "__main__":
    pytest.main()
