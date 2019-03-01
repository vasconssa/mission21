from math import *
import numpy as np

class Vector2D:

    def __init__(self, x=0.0, y=0.0):
        if hasattr(x, "__getitem__"):
            x, y = float(x[0]), float(x[1])
        self.v = np.array([x, y], dtype=np.float64)

    @staticmethod
    def fromCartesian(x=0.0, y=0.0):
        return Vector2D(x, y)

    @staticmethod
    def fromPolar(r, theta):
        return Vector2D(r*cos(theta), r*sin(theta))

    def x(self):
        return float(self.v[0])

    def y(self):
        return float(self.v[1])

    def length(self):
        return float(np.linalg.norm(self.v))

    def normalize(self):
        norm = np.linalg.norm(self.v)
        if norm != 0:
            self.v = self.v/norm

    def distance(self, p):
        return sqrt(np.linalg.norm(selv.v - p))

    def angle(self, w):
        return acos( (self*w)/(np.linalg.norm(self.v)*np.linalg.norm(w.v)) )

    def rotate(self, angle):
        angRadian = (angle*np.pi)/180.0
        x = cos(angRadian)*self[0] - sin(angRadian)*self[1]
        y = sin(angRadian)*self[0] + cos(angRadian)*self[1]
        self[0] = x
        self[1] = y
        return self

    def rotated(self, angle):
        vec = self
        vec.rotate(angle)
        return vec

    def __str__(self):
        return "(%s, %s)" % (self.v[0], self.v[1])

    def __repr_(self):
        return "Vector2D(%s, %s)" % (self.v[0], self.v[1])

    def __len__(self):
        return 2

    def __getitem__(self, index):
        return float(self.v[index])

    def __setitem__(self, index, value):
        self.v[index] = 1.0*value

    def __eq__(self, rhs):
        return np.all(self.v == rhs.v)

    def __ne__(self, rhs):
        return np.all(self.v != rhs.v)

    def __add__(self, rhs):
        return Vector2D(self.v + rhs.v)

    def __radd__(self, lhs):
        return Vector2D(self.v + lhs.v)

    def __iadd__(self, rhs):
        self.v += rhs.v
        return self

    def __sub__(self, rhs):
        return Vector2D(self.v - rhs.v)

    def __rsub__(self, lhs):
        return Vector2D(lhs.v - selv.v)

    def __isub__(self, rhs):
        self.v -= rhs.v
        return self

    def __mul__(self, rhs):
        if hasattr(rhs, "__getitem__"):
            return (self.v@rhs.v)
        else:
            return Vector2D(self.v*rhs)

    def __imul__(self, rhs):
            self.v *= rhs
            return self

    def __rmul__(self, lhs):
        if hasattr(lhs, "__getitem__"):
            return (self.v@lhs.v)
        else:
            return Vector2D(self.v*lhs)

    def __truediv__(self, rhs):
        if hasattr(rhs, "__getitem__"):
            return Vector2D(np.divide(self.v,rhs.v))
        else:
            return Vector2D(self.v/rhs)

    def __itruediv__(self, rhs):
        if hasattr(rhs, "__getitem__"):
            self.v = np.divide(self.v, rhs.v)
        else:
            self.v = self.v / rhs
        return self


    def __rtruediv__(self, lhs):
        if hasattr(lhs, "__getitem__"):
            return Vector2D(np.divide(lhs.v, self.v))

    def __pos__(self):
        return self.copy()

    def __neg__(self):
        return Vector2D(-self.v)
