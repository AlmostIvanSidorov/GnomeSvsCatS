import os


def decorator_func(class_func):
    def wrap_func(self):
        print("___________+++++++++++____________")
        print(class_func(self))
        print("___________+++++++++++____________")

    return wrap_func


def decorator_func2(input_func):
    def wrap_func(self):
        print("some-------------some")
        print(input_func(self))
        print("some_____________some")

    return wrap_func


class Student:
    def __init__(self, surname, name, second_name):
        self.name = name
        self.surname = surname
        self.second_name = second_name

    @decorator_func
    def name_func(self):
        return f"Student name is {self.surname} {self.name}  {self.second_name}"


class Score(Student):
    def __init__(self, surname, name, second_name, *score, **lesson_score):
        super().__init__(surname, name, second_name)
        self.score = score
        self.lesson_score = lesson_score

    def score_func(self):
        for marks in self.score:
            print(marks)
        for lesson, score in self.lesson_score.items():
            print(f"{lesson}: {score}")

    @decorator_func
    def factorial_class_func(self):
        number = self.score[0]

        def rec_fact(n):
            if n == 1:
                return n
            else:
                return n * rec_fact(n - 1)

        return rec_fact(number)


class Score2(Score):
    def __init__(self, word, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.word = word

    @decorator_func2
    def say_word(self):
        word_str = self.word + " "

        def rec_func(word):
            if len(word) < 30:
                return rec_func(word + word)
            else:
                return word

        return f"{self.name} says " + rec_func(word_str)


def main():
    secondname = os.getenv("NEW_VAR")

    student1 = Score(
        "Sidorov", "Ivan", f"{secondname}", 5, 50, 30, math=100, baseball=1000
    )

    student1.name_func()
    student1.score_func()
    student1.factorial_class_func()

    student2 = Score2(
        "Hello!", "Sidorov", "Ira", f"{secondname}", 8, 50, 30, math=100, baseball=1000
    )
    student2.say_word()

    print(Score2.__mro__)


if __name__ == "__main__":
    main()
