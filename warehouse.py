def warehouseProcess(d, transaction):
    command, resource, amt = transaction
    if command == 'ship': d[resource] -= amt
    elif command == 'receive':
        if resource not in d: d[resource] = amt
        else: d[resource] += amt

class Warehouse:
    def __init__(self):
        self.dict = {}

    def process(self, transaction):
        warehouseProcess(self.dict, transaction)

    def lookup(self, commodity):
        if commodity in self.dict: return self.dict[commodity]
        return 0

w = Warehouse()
w.process(('receive', 'a', 10))
w.process(('ship', 'a', 7))
print(w.lookup('a'))
print(w.lookup('b'))
