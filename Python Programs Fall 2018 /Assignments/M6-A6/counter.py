import random


class Counter:
    def __init__(self):
        self.count = 0

    def get_Value(self):
        return self.count

    def set_value(self, count):
        self.count = count


counterForHeads = Counter()
counterForTails = Counter()

for i in range(0, 101):
    coinValue = random.randint(0, 2)

    if coinValue == 0:
        counterForHeads.count += 1
    else:
        counterForTails.count += 1

print(1 + 1)
