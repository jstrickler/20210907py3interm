
class Cat:
    def meow(self):
        print("Meow meow meow")

c1 = Cat()
c2 = Cat()
c1.meow()
c2.meow()
print()

def bark(self):
    print("Woof woof woof")

Dog = type('Dog', (), {'bark': bark})

d1 = Dog()
d1.bark()

