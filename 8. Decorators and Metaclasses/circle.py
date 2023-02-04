import math

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

    @classmethod
    def from_points(cls, points):
        x12 = points[0].x - points[1].x
        x13 = points[0].x - points[2].x

        y12 = points[0].y - points[1].y
        y13 = points[0].y - points[2].y

        y31 = points[2].y - points[0].y
        y21 = points[1].y - points[0].y

        x31 = points[2].x - points[0].x
        x21 = points[1].x - points[0].x

        # x1^2 - x3^2
        sx13 = pow(points[0].x, 2) - pow(points[2].x, 2)
        # y1^2 - y3^2
        sy13 = pow(points[0].y, 2) - pow(points[2].y, 2)

        sx21 = pow(points[1].x, 2) - pow(points[0].x, 2)
        sy21 = pow(points[1].y, 2) - pow(points[0].y, 2)

        f = ((sx13 * x12 + sy13 * x12 + sx21 * x13 + sy21 * x13) // (2 * (y31 * x12 - y21 * x13)))
        g = ((sx13 * y12 + sy13 * y12 + sx21 * y13 + sy21 * y13) // (2 * (x31 * y12 - x21 * y13)))
        c = (-pow(points[0].x, 2) - pow(points[0].y, 2) - 2 * g * points[0].x - 2 * f * points[0].y)

        # eqn of circle be x^2 + y^2 + 2*g*x + 2*f*y + c = 0
        # where centre is (h = -g, k = -f) and
        # radius r as r^2 = h^2 + k^2 - c
        centre_h = -g
        centre_k = -f
        sqr_of_r = pow(centre_h, 2) + pow(centre_k, 2) - c
        # r is the radius
        radius = round(math.sqrt(sqr_of_r), 2)
        return Circle(centre_h, centre_k, radius)

    @property
    def top(self):
        return self.pt.y + self.radius

    @property
    def left(self):
        return self.pt.x - self.radius

    @property
    def right(self):
        return self.pt.x + self.radius

    @property
    def bottom(self):
        return self.pt.y - self.radius

    @property
    def height(self):
        return self.top - self.bottom

    @property
    def width(self):
        return self.right - self.left

    @property
    def topleft(self):
        return Point(self.top, self.left)

    @property
    def topright(self):
        return Point(self.top, self.right)

    @property
    def bottomleft(self):
        return Point(self.bottom, self.left)

    @property
    def bottomright(self):
        return Point(self.bottom, self.right)
