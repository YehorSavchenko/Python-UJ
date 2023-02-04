import unittest


class Poly:

    def __init__(self, c=0, n=0):
        self.size = n + 1
        self.wspolczyniki = self.size * [0]
        self.wspolczyniki[n] = c
        self.reduce_stopien()

    def __str__(self):
        return str(self.wspolczyniki)

    def __add__(self, other):
        new_stopien = max(self.stopien, other.stopien)
        result_Poly = Poly(0, new_stopien)

        for i in range(other.stopien + 1):
            result_Poly.wspolczyniki[i] += other.wspolczyniki[i]

        for i in range(self.stopien + 1):
            result_Poly.wspolczyniki[i] += self.wspolczyniki[i]

        result_Poly.reduce_stopien()
        return result_Poly

    def __sub__(self, other):
        new_stopien = max(self.stopien, other.stopien)
        result_Poly = Poly(0, new_stopien)

        for i in range(other.stopien + 1):
            result_Poly.wspolczyniki[i] -= other.wspolczyniki[i]

        for i in range(self.stopien + 1):
            result_Poly.wspolczyniki[i] += self.wspolczyniki[i]

        result_Poly.reduce_stopien()
        return result_Poly

    def __mul__(self, other):
        new_stopien = self.stopien + other.stopien
        result_Poly = Poly(0, new_stopien)

        for i in range(self.stopien + 1):
            for j in range(other.stopien + 1):
                result_Poly.wspolczyniki[i + j] += self.wspolczyniki[i] * other.wspolczyniki[j]

        result_Poly.reduce_stopien()
        return result_Poly

    def __pos__(self):
        return self

    def __neg__(self):
        self.wspolczyniki = list(map(lambda x: x * (-1), self.wspolczyniki))
        return self

    def eval(self, x):
        result = self.wspolczyniki[self.stopien]
        for i in range(1, self.stopien + 1):
            result = (result * x) + self.wspolczyniki[self.stopien - i]

        return result

    def is_zero(self):
        return all(item == 0 for item in self.wspolczyniki)

    def __eq__(self, other):
        return self.wspolczyniki == other.wspolczyniki

    def __ne__(self, other):
        return self.wspolczyniki != other.wspolczyniki

    def combine(self, other):
        result_Poly = Poly(0, 0)
        for i in range(self.stopien, -1, -1):
            term = Poly(self.wspolczyniki[i], 0)
            result_Poly = term + (other * result_Poly)
        return result_Poly

    def __pow__(self, n):
        result_Poly = self
        for i in range(1, n):
            result_Poly = result_Poly * result_Poly
        return result_Poly

    def diff(self):
        if self.stopien == 0:
            return Poly(0, 0)
        result_Poly = Poly(0, self.stopien - 1)
        result_Poly.stopien = self.stopien - 1

        for i in range(self.stopien):
            result_Poly.wspolczyniki[i] = (i + 1) * self.wspolczyniki[i + 1]
        return result_Poly

    def reduce_stopien(self):
        self.stopien = -1
        for i in range(len(self.wspolczyniki) - 1, -1, -1):
            if self.wspolczyniki[i] != 0:
                self.stopien = i
                return


class TestPolynomials(unittest.TestCase):
    def setUp(self):
        self.p0 = Poly(0, 2)
        self.p1 = Poly(1, 1)
        self.p2 = Poly(1, 2)
        self.p3 = Poly(4, 3) + (Poly(3, 2)) + (Poly(2, 1)) + (Poly(1, 0))
        self.p4 = Poly(3, 2) + (Poly(5, 0))
        self.p5 = Poly(3, 2) + (Poly(5, 0))
        self.p6 = Poly(3, 2) + (Poly(5, 0)) + (Poly(0, 4))
        self.p7 = Poly(-4, 3) + (Poly(3, 2)) + (Poly(-2, 1)) + (Poly(1, 0))

    def test___add__(self):
        self.assertEqual([0, 1, 1], (self.p1 + self.p2).wspolczyniki)
        self.assertEqual([6, 2, 6, 4], (self.p3 + self.p4).wspolczyniki)

    def test___sub__(self):
        self.assertEqual([0, 0, 0, 0], (self.p3 - self.p3).wspolczyniki)
        self.assertEqual([-1, -2, -3, -4], (self.p0 - self.p3).wspolczyniki)

    def test___mul__(self):
        self.assertEqual([5, 10, 18, 26, 9, 12], (self.p3 * self.p4).wspolczyniki)

    def test___pos__(self):
        self.assertEqual([1, -2, 3, -4], (+self.p7).wspolczyniki)

    def test___neg__(self):
        self.assertEqual([-1, 2, -3, 4], (-self.p7).wspolczyniki)

    def test_is_zero(self):
        self.assertTrue(self.p0.is_zero())

    def test___eq__(self):
        self.assertTrue(self.p4 == self.p5)
        self.assertTrue(self.p5 == self.p6)
        self.assertFalse(self.p5 == self.p2)

    def test___ne__(self):
        self.assertFalse(self.p4 != self.p5)
        self.assertFalse(self.p5 != self.p6)
        self.assertTrue(self.p5 != self.p2)

    def test_eval(self):
        self.assertEqual(142, self.p3.eval(3))

    def test_combine(self):
        self.assertEqual([586, 0, 996, 0, 567, 0, 108], self.p3.combine(self.p4).wspolczyniki)

    def test___pow__(self):
        self.assertEqual([1, 4, 10, 20, 25, 24, 16], (self.p3 ** 2).wspolczyniki)

    def test_diff(self):
        self.assertEqual([2, 6, 12], self.p3.diff().wspolczyniki)
        self.assertEqual([6, 24], self.p3.diff().diff().wspolczyniki)

    def tearDown(self):
        del self.p0, self.p1, self.p2, self.p3, self.p4, self.p5


if __name__ == '__main__':
    unittest.main()
