import unittest


def add_poly(poly1, poly2):
    stopien = max(len(poly1) - 1, len(poly2) - 1)
    poly_result = [0 for _ in range(stopien + 1)]

    for i in range(len(poly2)):
        poly_result[i] += poly2[i]

    for i in range(len(poly1)):
        poly_result[i] += poly1[i]

    reduce_stopien(poly_result)
    return poly_result


def sub_poly(poly1, poly2):
    stopien = max(len(poly1) - 1, len(poly2) - 1)
    poly_result = [0 for _ in range(stopien + 1)]

    for i in range(len(poly2)):
        poly_result[i] -= poly2[i]

    for i in range(len(poly1)):
        poly_result[i] += poly1[i]

    reduce_stopien(poly_result)
    return poly_result


def mul_poly(poly1, poly2):
    stopien = len(poly1) - 1 + len(poly2) - 1
    poly_result = [0 for _ in range(stopien + 1)]

    for i in range(len(poly1)):
        for j in range(len(poly2)):
            poly_result[i + j] += poly1[i] * poly2[j]

    reduce_stopien(poly_result)
    return poly_result


def eval_poly(poly, x):
    result = poly[len(poly) - 1]
    for i in range(1, len(poly)):
        result = (result * x) + poly[len(poly) - 1 - i]

    return result


def is_zero(poly):
    return all(item == 0 for item in poly)


def eq_poly(poly1, poly2):
    reduce_stopien(poly1)
    reduce_stopien(poly2)
    return poly1 == poly2


def combine_poly(poly1, poly2):
    poly_result = [0]
    for i in range(len(poly1) - 1, -1, -1):
        temp = [poly1[i]]
        poly_result = add_poly(temp, mul_poly(poly2, poly_result))
    return poly_result


def pow_poly(poly1, n):
    poly_result = poly1
    for i in range(1, n):
        poly_result = mul_poly(poly_result, poly_result)
    return poly_result


def diff_poly(poly1):
    if (len(poly1) - 1) == 0:
        return [0]
    poly_result = [0 for _ in range(len(poly1) - 1)]

    for i in range(len(poly1) - 1):
        poly_result[i] = (i + 1) * poly1[i + 1]
    return poly_result


def reduce_stopien(poly):
    for i in range(len(poly) - 1, -1, -1):
        if poly[i] != 0:
            return
        elif i != 0:
            del poly[i]


class TestPolynomials(unittest.TestCase):
    def setUp(self):
        self.p0 = [0, 0, 0]
        self.p1 = [0, 1]
        self.p2 = [0, 0, 1]
        self.p3 = [1, 2, 3, 4]
        self.p4 = [5, 0, 3]
        self.p5 = [5, 0, 3]
        self.p6 = [5, 0, 3, 0]

    def test_add_poly(self):
        self.assertEqual([0, 1, 1], add_poly(self.p1, self.p2))
        self.assertEqual([6, 2, 6, 4], add_poly(self.p3, self.p4))

    def test_sub_poly(self):
        self.assertEqual([0], sub_poly(self.p3, self.p3))
        self.assertEqual([-1, -2, -3, -4], sub_poly(self.p0, self.p3))

    def test_mul_poly(self):
        self.assertEqual([5, 10, 18, 26, 9, 12], mul_poly(self.p3, self.p4))

    def test_is_zero(self):
        self.assertTrue(is_zero(self.p0))

    def test_eq_poly(self):
        self.assertTrue(eq_poly(self.p4, self.p5))
        self.assertTrue(eq_poly(self.p5, self.p6))

    def test_eval_poly(self):
        self.assertEqual(142, eval_poly(self.p3, 3))

    def test_combine_poly(self):
        self.assertEqual([586, 0, 996, 0, 567, 0, 108], combine_poly(self.p3, self.p4))

    def test_pow_poly(self):
        self.assertEqual([1, 4, 10, 20, 25, 24, 16], pow_poly(self.p3, 2))

    def test_diff_poly(self):
        self.assertEqual([2, 6, 12], diff_poly(self.p3))
        self.assertEqual([6, 24], diff_poly(diff_poly(self.p3)))

    def tearDown(self):
        del self.p0, self.p1, self.p2, self.p3, self.p4, self.p5


if __name__ == '__main__':
    unittest.main()
