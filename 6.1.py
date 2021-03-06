import math


class Point:

    def __init__(self, x=0, y=0):
        """A 2D cartesian coordinate
        >>> point = Point()
        >>> point
        Point(0, 0)
        """
        self.x = x
        self.y = y


    def distance_from_origin(self):
        """Returns the distance of the point from the origin
        >>> point = Point(3, 4)
        >>> point.distance_from_origin()
        5.0
        """
        return math.hypot(self.x, self.y)


    def __add__(self, other):
        """Returns a new Point whose coordinate are the sum of this
        one's and the other one's
        >>> p = Point(2, 4)
        >>> q = p + Point(3, 5)
        >>> q
        Point(5, 9)
        """
        return Point(self.x + other.x, self.y + other.y)


    def __iadd__(self, other):
        """Returns this Point with its coordinate set to the sum of this
        one's and the other one's
        >>> p = Point(2, 4)
        >>> p += Point(3, 5)
        >>> p
        Point(5, 9)
        """
        self.x += other.x
        self.y += other.y
        return self


    def __sub__(self, other):
        """Returns a new Point whose coordinate are the difference of this
        one's and the other one's
        >>> p = Point(2, 4)
        >>> q = p - Point(3, 5)
        >>> q
        Point(-1, -1)
        """
        return Point(self.x - other.x, self.y - other.y)


    def __isub__(self, other):
        """Returns this Point with its coordinate set to the difference
        of this one's and the other one's
        >>> p = Point(2, 4)
        >>> p -= Point(3, 5)
        >>> p
        Point(-1, -1)
        """
        self.x -= other.x
        self.y -= other.y
        return self


    def __mul__(self, other):
        """Returns a new Point whose coordinate is this one's multiplied
        by the other number
        >>> p = Point(2, 4)
        >>> q = p * 3
        >>> q
        Point(6, 12)
        """
        return Point(self.x * other, self.y * other)


    def __imul__(self, other):
        """Returns this Point with its coordinate set to this one's
        multiplied by the other number
        >>> p = Point(2, 4)
        >>> p *= 3
        >>> p
        Point(6, 12)
        """
        self.x *= other
        self.y *= other
        return self


    def __truediv__(self, other):
        """Returns a new Point whose coordinate is this one's divided
        by the other number
        >>> p = Point(2, 4)
        >>> q = p / 2
        >>> q
        Point(1.0, 2.0)
        """
        return Point(self.x / other, self.y / other)


    def __itruediv__(self, other):
        """Returns this Point with its coordinate set to this one's
        divided by the other number
        >>> p = Point(2, 4)
        >>> p /= 2
        >>> p
        Point(1.0, 2.0)
        """
        self.x /= other
        self.y /= other
        return self


    def __floordiv__(self, other):
        """Returns a new Point whose coordinate is this one's floor
        divided by the other number
        >>> p = Point(2, 4)
        >>> q = p // 2
        >>> q
        Point(1, 2)
        """
        return Point(self.x // other, self.y // other)


    def __ifloordiv__(self, other):
        """Returns this Point with its coordinate set to this one's
        floor divided by the other number
        >>> p = Point(2, 4)
        >>> p //= 2
        >>> p
        Point(1, 2)
        """
        self.x //= other
        self.y //= other
        return self


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def __repr__(self):
        return "Point({0.x!r}, {0.y!r})".format(self)


    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)


class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        """A Circle
        >>> circle = Circle(2)
        >>> circle
        Circle(2, 0, 0)
        """
        super().__init__(x, y)
        self.radius = radius


    def edge_distance_from_origin(self):
        """The distance of the circle's edge from the origin
        >>> circle = Circle(2, 3, 4)
        >>> circle.edge_distance_from_origin()
        3.0
        """
        return abs(self.distance_from_origin() - self.radius)


    def area(self):
        """The circle's area
        >>> circle = Circle(3)
        >>> a = circle.area()
        >>> int(a)
        28
        """
        return math.pi * (self.radius ** 2)


    def circumference(self):
        """The circle's circumference
        >>> circle = Circle(3)
        >>> d = circle.circumference()
        >>> int(d)
        18
        """
        return 2 * math.pi * self.radius


    def __eq__(self, other):
        return self.radius == other.radius and super().__eq__(other)


    def __repr__(self):
        return "Circle({0.radius!r}, {0.x!r}, {0.y!r})".format(self)


    def __str__(self):
        return repr(self)
        

if __name__ == "__main__":
    import doctest
    doctest.testmod()

