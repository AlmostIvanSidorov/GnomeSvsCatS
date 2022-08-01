#!/usr/bin/env python3
import os


# Тз: 4 класса один с мульти наследованием и *args **kwargs каждый имеет по декоратору и одному методу с рекурсией +
# какую нибудь простенькую логику на инпут и вызов методов из каждого класса, пароль токен


def family_who_dec(orig_func):
    def wrap(self):
        print("+++++++++++++++++++")
        print(orig_func(self))
        print("+++++++++++++++++++")

    return wrap


def person_name_dec(orig_func):
    def wrap(self):
        print("-----------------")
        print(orig_func(self))
        print("-----------------")

    return wrap


def pet_meaw_dec(orig_func):
    def wrap(self):
        print(
            "──────▄▀▄─────▄▀▄\n"
            "─────▄█░░▀▀▀▀▀░░█▄\n"
            "─▄▄──█░░░░░░░░░░░█──▄▄\n"
            "█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█\n"
        )
        print(orig_func(self))
        return orig_func(self)
    wrap.unwrapped = orig_func
    return wrap


def super_init_dec(orig_func):
    def wrap(self, *args, **kwargs):
        print(
            "▒▒▄▀▀▀▀▀▄▒▒▒▒▒▄▄▄▄▄▒▒▒\n"
            "▒▐░▄░░░▄░▌▒▒▄█▄█▄█▄█▄▒\n"
            "▒▐░▀▀░▀▀░▌▒▒▒▒▒░░░▒▒▒▒\n"
            "▒▒▀▄░═░▄▀▒▒▒▒▒▒░░░▒▒▒▒\n"
            "▒▒▐░▀▄▀░▌▒▒▒▒▒▒░░░▒▒▒▒\n"
        )
        orig_func(self, *args, **kwargs)

    return wrap


class Family:
    def __init__(self, surname):
        self.surname = surname

    @family_who_dec
    def who_are_we(self):
        return f"We are {self.surname}"


class Person(Family):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    @person_name_dec
    def my_name(self):
        return f"My name is {self.name}"


class Pet(Family):
    meow = "meow! "

    def __init__(self, nickname, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nickname = nickname

    @pet_meaw_dec
    def meow(self, meow=meow):
        meow = meow

        def rec_func(signal):
            if len(signal) > 30:
                return signal
            else:
                return rec_func(signal.capitalize() + signal.upper())

        return rec_func(meow)

    def my_nickname(self):
        print(f"My name is {self.nickname}")


class SuperHuman(Person, Pet):
    super_meow = "supermeow"

    @super_init_dec
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @pet_meaw_dec
    def super_meow(self, super_meow=super_meow):
        strv = super().meow(super_meow)
        return strv


def main():
    program = True
    password_tok = os.getenv("PASS_VAR")
    while program:
        password = input("Enter password: ")
        if password == password_tok:
            member1 = Person("Ira", "Sidorovy")
            member2 = Person("Ivan", "Sidorovy")
            pet1 = Pet("Ricus", "Sidorovy")
            pet2 = Pet("Morty", "Sidorovy")
            stepa = SuperHuman("Stepa", "Steplik", "Sidorovy")
            family_member_list = [member1, member2, stepa]
            family_pet_list = [pet1, pet2, stepa]

            for unit in family_member_list:
                unit.who_are_we()
                unit.my_name()

            for unit in family_pet_list:
                print("MUUUUUUUUUUURRRRRR!!!")
                unit.my_nickname()
                unit.who_are_we()
                unit.meow()

            stepa.super_meow()
            print(SuperHuman.__mro__)

        elif password == "exit":
            program = False
        else:
            print('You shall not pass, print "exit" if you want to run away!')


if __name__ == "__main__":
    main()
