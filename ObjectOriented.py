import math

class NameOfClass():
    """
    My first tested class!
    """

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        print(self.param1+f" Ivanself.param2 {self.param2}")


# NameOfClass(param1="you", param2="she").some_method()
# unit = NameOfClass(param1='You are', param2='she1')
#
# unit.param2 = ' incredible!'
#
# print(type(unit))
# unit.some_method()





class Animal():
    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


class Circle(Animal):
    #Class object
    pi = 3.14

    def __init__(self, radius=1):
        Animal.__init__(self)

        self.radius = radius
        self.area = radius*radius*Circle.pi

    #Method
    def get_circumference(self):
        return self.radius*Circle.pi*2


class Book:

    def __init__(self, title, author, pages):

        self.author = author
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book title:{self.title} author: {self.author}"

    def __len__(self):
        return self.pages


my_book = Book(title="'From Begginer To Leader'", author="IvanS", pages=200)

print(my_book)

print(len(my_book))

class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return math.sqrt(pow((self.coor1[0]-self.coor2[0]), 2) + pow((self.coor1[1]-self.coor2[1]), 2))

    def slope(self):
        return (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])


class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, pay):
        self.balance = self.balance + pay
        print(f"Deposit Accepted. Now your balance: {self.balance}")

    def withdraw(self, withdraw_pay):
        if self.balance >= withdraw_pay:
            self.balance = self.balance - withdraw_pay
            print(f"Withdrawal Accepted. Now your balance: {self.balance}")
        else:
            print(f"Not enough money, your balance is {self.balance}")

    def __str__(self):
        return f"Account owner: {self.owner} \nAccount balance: {self.balance}"


# acct1 = Account('Ivan', 100)
#
# print(acct1)
#
# print(acct1.owner, acct1.balance)
#
# acct1.deposit(50)
#
# acct1.withdraw(75)
#
# acct1.withdraw(500)

class Dog:
    def __init__(self, breed):
        self.breed = breed

my_dog = Dog(breed='lab')

print(my_dog.breed)


