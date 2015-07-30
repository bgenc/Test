__author__ = 'bgenc'

import math

class RN:
    def __init__(self, p_c, p_a, p_b):
        self.a = int(p_a)
        self.b = int(p_b)
        self.c = int(p_c)
        self.simplify()

    def simplify(self):
        if self.a == 0:
            return

        if self.b < 0:
            self.b *= -1
            self.a *= -1
            self.simplify()
            return

        if abs(self.a) >= self.b:
            self.c += self.a / self.b
            self.a %= self.b
            self.simplify()
            return

        if self.c > 0 > self.a:
            self.a += self.b
            self.c -= 1
            self.simplify()
            return

        if self.c < 0 < self.a:
            self.a += -self.b
            self.c += 1
            self.simplify()
            return

        if (not (self.a == 1 or self.a == -1)) and self.b % self.a == 0:
            self.b /= abs(self.a)
            self.a /= abs(self.a)
            self.simplify()
            return

        if self.a % 2 == 0 and self.b % 2 == 0:
            self.a /= 2
            self.b /= 2
            self.simplify()
            return

        for i in (x for x in range(3, max(4, int(math.sqrt(abs(self.a))+1))) if x % 2 is not 0):
            if self.a % i == 0 and self.b % i == 0:
                self.a /= i
                self.b /= i
                self.simplify()
                break

        return

    def __add__(self, other):
        if isinstance(other, int):
            return RN(self.c + other, self.a, self.b)
        else:
            return RN(self.c + other.c, self.a * other.b + self.b * other.a, self.b * other.b)

    def __radd__(self, other):
        if isinstance(other, int):
            return RN(self.c + other, self.a, self.b)
        else:
            return RN(self.c + other.c, self.a * other.b + self.b * other.a, self.b * other.b)

    def __sub__(self, other):
        return RN(self.c - other.c, self.a * other.b - self.b * other.a, self.b * other.b)

    def __mul__(self, other):
        return RN(0, (self.a + self.b * self.c) * (other.a + other.b * other.c), self.b * other.b)

    def __div__(self, other):
        return RN(0, (self.a + self.b * self.c) * other.b, (other.a + other.b * other.c) * self.b)

    def __str__(self):
        if self.a == 0:
            return str(self.c)

        if self.c is not 0:
            if self.a >= 0:
                return str(self.c) + "+" + str(self.a) + "/" + str(self.b)
            else:
                return str(self.c) + "-" + str(abs(self.a)) + "/" + str(self.b)
        else:
            return str(self.a) + "/" + str(self.b)

print 1 + RN(0, 1, 2)