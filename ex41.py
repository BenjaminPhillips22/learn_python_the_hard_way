# Class' and Objects


class Person:
    """
    This is the doc for a person,
    Is it cool? We'll see.
    """
    personCount = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.personCount += 1

    def displayCount(self):
        print(f"Total Person count is; {Person.personCount}")

    def displayPerson(self):
        print("Name :", self.name, "Age: ", self.age)


p1 = Person(name="Zara", age=99)
p2 = Person(name="Manni", age=12)
p1.displayPerson()
p2.displayPerson()
p1.displayCount()

# We can also use 'hasattr', 'getattr', 'setattr' and 'delattr'
print(hasattr(p1, 'name'))
print(getattr(p1, 'name'))
print(setattr(p1, 'name', 'Zara P'))
print(delattr(p2, 'age'))
try:
    p2.displayPerson()
except AttributeError:
    print("There was an attribute error")

# There are some built in class attributes

print(Person.__doc__)
print(Person.__name__)
print(Person.__module__)
print(Person.__bases__)
print(Person.__dict__)

print(p1.__class__)
print(p1.__getattribute__('name'))
