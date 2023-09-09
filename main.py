class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

first_person = Person("mohammad", 22)

print(f"My name is {first_person.name} and I am {first_person.age} years old")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        if self.age > 18:
            print("You have too much responsibilities")
        else:
            print("Lucky you")

second_person = Person("Ahmad", 17)

second_person.is_adult()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        if self.age > 18:
            print("You have too much responsibilities")
        else:
            print("Lucky you")

    def __str__(self):
        return f"My name is {self.name} and I am {self.age} years old"


third_person = Person("abdullah", 25)


print(third_person)
