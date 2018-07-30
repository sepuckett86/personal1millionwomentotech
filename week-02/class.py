class Fruit():
    def __init__(self, name, taste):
        self.name = name
        self.taste = taste
    def fruit_print(self):
        print(self.name + ' is ' + self.taste)

f1 = Fruit('watermelon', 'sweet')

print(f1)
print(f1.name)
print(f1.taste)
f1.fruit_print()
