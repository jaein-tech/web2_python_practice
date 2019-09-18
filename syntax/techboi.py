class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("hi " + to_name + " i'm " + self.name)

    def introduce(self):
        print("my name " + self.name + " and i'm " + str(self.age) + "years old")


class Police(Person):
    def arrest(self, to_arrest):
        print("you arrest, " + to_arrest)

class Programmer(Person):
    def program(self, to_program):
        print("what I make next? " + to_program)


jaein = Person("jaein", 24)
bob = Police("bob", 28)
jenny = Programmer("jenny", 30)

bob.arrest("minu")
jenny.program("python")
jaein.introduce()
