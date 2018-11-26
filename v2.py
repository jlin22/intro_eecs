class V2:
    # two dimensional vector
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __add__(self, other):
        return V2(self.x + other.x, self.y + other.y)

    def __mul__(self, c):
        return V2(c * self.x, c * self.y)

# testing the 2d vector class
v1 = V2(3, 4)
print(v1)
print(v1.getX(), v1.getY())
v2 = V2(12, 13)
print(v1 + v2)
