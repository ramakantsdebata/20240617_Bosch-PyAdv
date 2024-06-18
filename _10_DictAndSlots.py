class MyClass:
    def __init__(self, name) -> None:
        self.name = name


# obj1 = MyClass("Abhijeet")
# print(obj1.name)
# obj1.city = "Hyderabad"
# print(obj1.city)

# print(MyClass("Pravin").__dict__['name'])

obj1 = MyClass("Pravin")
print(obj1.__dict__)
print(isinstance(obj1, MyClass))

obj2 = MyClass("Manish")
obj2.city = "Hyderabad"
del obj2.name
print(obj2.__dict__)
print(isinstance(obj2, MyClass))

print("\n\n", "="* 80)
class Point:
    __slots__ = ['x', 'y']      # << What type of attribute is this ?

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return f"x[{self.x}], y[{self.y}]"
    
p1 = Point(10, 20)
print(p1)
# p1.z = 30

print(f"{p1!r}")
# print(p1.__dict__)
p1.__slots__.append('z')
print(p1.__slots__)
# p1.z = 30  # <-- ERROR
