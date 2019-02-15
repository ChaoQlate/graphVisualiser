import math
class vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def unitVector(self):
        d = self.length()
        if d == 0:
            return None
        return vector(self.x/d, self.y/d)

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y if type(other) == type(self) else False

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("must be {} not {}".format(vector, type(other)))
        return vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        if type(self) != type(other):
            raise TypeError("must be {} not {}".format(vector, type(other)))
        return vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if type(other) not in [int, float]:
            raise TypeError("scalar multiplier must be int or float not {}".format(type(other)))
        return vector(self.x * other, self.y * other)
    
    def __div__(self, other):
        if type(other) not in [int, float]:
            raise TypeError("scalar divisor must be int or float not {}".format(type(other)))
        return vector(self.x / other, self.y / other)

    def __iadd__(self, other):
        if type(other) != type(self):
            raise TypeError("must be {} not {}".format(vector, type(other)))
        self.x += other.x
        self.y += other.y
        return self

    def __str__(self):
        return "(" + str(round(self.x, 3)) + "," + str(round(self.y, 3)) + ")"
    
    def __repr__(self):
        return self.__str__()