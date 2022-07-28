class Famally:

    def __init__(self, surname):
        self.surname = surname

    def love(self):
        print(f"loves {self.surname} famally")


class Famally_persona(Famally):

    def __init__(self, surname, name):
        super(Famally_persona, self).__init__(surname)
        self.name = name

    def my_name(self):
        print(f"My name is {self.name} {self.surname}")


class Famally_pet(Famally, Famally_persona):

    def __init__(self, surname, nickname):
        super(Famally).__init__(surname)
        self.nickname = nickname

    def love(self, surname):

        return super(Famally_pet, self).love()


ivan = Famally_persona(name="Ivan", surname="Sidorov")

print(Famally_pet.__mro__, ivan.my_name(), ivan.love())



