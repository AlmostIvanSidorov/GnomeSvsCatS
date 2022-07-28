import os

class Emp():
    def __init__(self, id, name, add):
        self.id = id
        self.name = name
        self.add = add


# Class freelancer inherits EMP
class Freelance(Emp):
    def __init__(self, id, name, add, emails):
        super().__init__(id, name, add)
        self.emails = emails

# --Prog2--

class Animals:

    # Initializing constructor
    def __init__(self, mammals=True):
        self.legs = 4
        self.domestic = True
        self.tail = True
        self.mammals = mammals

    def isMammal(self):
        if self.mammals:
            print("It is a mammal.")

    def isDomestic(self):
        if self.domestic:
            print("It is a domestic animal.")


class Dogs(Animals):
    def __init__(self, mammals):
        super().__init__(mammals=mammals)

    # def isMammal(self):
    #     super().isMammal()


class Horses(Animals):
    def __init__(self):
        super().__init__()

    def hasTailandLegs(self):
        if self.tail and self.legs == 4:
            print("Has legs and tail")

# --Prog3--
class Mammal2():
    def __init__(self, name):
        var = os.getenv("NEW_VAR")
        print(var)
        self.canFly_name = name
class canSwim(Mammal2):

    def __init__(self, canFly_name):
        print("2")
        super().__init__(canFly_name)

class canFly(Mammal2):

    def __init__(self, canFly_name):
        print("1")
        super().__init__(canFly_name)


class Animal2(canSwim, canFly):

    def __init__(self, name):
        # Calling the constructor
        # of both the parent
        # class in the order of
        # their inheritance
        super().__init__(name)


def prog1():
    emp_1 = Freelance(103, "Suraj kr gupta", "Noida", "KKK@gmails")
    print('The ID is:', emp_1.id)
    print('The Name is:', emp_1.name)
    print('The Address is:', emp_1.add)
    print('The Emails is:', emp_1.emails)


def prog2():
    # Driver code
    Tom = Dogs(mammals=True)
    Tom.isMammal()
    Bruno = Horses()
    Bruno.hasTailandLegs()


def prog3():
    var = os.getenv("NEW_VAR")
    bird = Animal2("Chuck")
    print(Animal2.__mro__)


if __name__ == "__main__":
    prog3()

