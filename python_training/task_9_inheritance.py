# class Mammal:
#     className = "Млекопитающие"
#
#
# class Dog(Mammal):
#     species = "Canis Lupus"
#
# dog = Dog()
# print(dog.className)

class A:
    def __init__(self):
        self.x = 10


class B(A):
    def __init__(self):
        super().__init__()
        self.y = self.x + 5


print(B().x)

b = B()
print(b.y)
