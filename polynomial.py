from math import sqrt

class Polynomial:
    def __init__(self, a):
        self.coefficients = a
    def __str__(self):
        a = ''
        for i in range(len(self.coefficients)):
            a += str(format(self.coefficients[i], '.3f'))
            if (len(self.coefficients) - i > 1):
                a += ' z**' + str(len(self.coefficients) - i - 1) + ' + '
            elif len(self.coefficients) - i  - 1 == 1:
                a += ' z + '
        return a
    def __add__(self, other):
        d = {}
        for i in range(max(len(self.coefficients), len(other.coefficients))):
            d.setdefault(i, 0)
        for i in range(len(self.coefficients)):
            d[len(self.coefficients) - 1 - i] += self.coefficients[i] 
        for i in range(len(other.coefficients)):
            d[len(other.coefficients) - 1 - i] += other.coefficients[i] 
        return Polynomial(list(reversed(list(d.values()))))

    def __mul__(self, other):
        d = {}
        for i in range((len(self.coefficients) + len(other.coefficients) - 1)):
            d.setdefault(i, 0)
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                d[(len(self.coefficients) - 1 - i) + (len(other.coefficients) - 1 - j)] += self.coefficients[i] * other.coefficients[j]
                self.coefficients[i] * other.coefficients[j]
        return Polynomial(list(reversed(list(d.values()))))
    
    def val(self, v):
        a = self.coefficients[0]
        for i in range(1, len(self.coefficients)):
            a *= v
            a += self.coefficients[i]
        return a

    def roots(self):
        if len(self.coefficients) > 3 or len(self.coefficients) <= 1: 
            return 'Order too high to solve for roots'
        if len(self.coefficients) == 2:
            return -self.coefficients[1] / self.coefficients[0]
        if len(self.coefficients) == 3:
            a, b, c = self.coefficients
            if b ** 2 - 4 * a * c < 0:
                return complex(-b, sqrt(abs(b ** 2 - 4 * a * c))) / (2 * a), complex(-b, -sqrt(abs(b ** 2 - 4 * a * c))) / (2 * a)
            else:
                return (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a), (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
         
        

p1 = Polynomial([1, 2, 1])
print(p1)
p2 = Polynomial([3, 4])
print(p1 + p2)
print(p2 + p1)
p3 = Polynomial([4, 5, 6])
print(p1 + p3)
print(p1 * p2)
p4 = Polynomial([3, -4])
print(p2 * p4)

print(p2.val(2))
print(p1.roots())
print(p3.roots())
print(p2.roots())

