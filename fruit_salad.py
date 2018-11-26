class FruitSalad:
    fruits = ['melons', 'pineapples']
    servings = 4
    
    def __init__(self, ingredients, numservings):
        self.fruits = ingredients
        self.servings = numservings

    def __str__(self):
        return str(self.servings) + ' servings of fruit salad with ' + str(self.fruits)

    def add(self, f):
        self.fruits.append(f)

    def serve(self):
        if self.servings == 0:
            return 'Sorry!'
        else:
            self.servings -= 1
            return 'Enjoy!'
    
fs = FruitSalad(['banana', 'apple'], 4)
print(fs)
fs.add('coconut')
print(fs)
for i in range(6):
    print(str(i) + ' ' + fs.serve())
