import os
def decorator_func(class_func):
    def wrap_func(self):
        print("___________+++++++++++____________")
        print(class_func(self))
        print("___________+++++++++++____________")
    return wrap_func


class Student:
    def __init__(self, name, surname, second_name):
        self.name = name
        self.surname = surname
        self.second_name = second_name

    @decorator_func
    def name_func(self):
        return f"Student name is {self.name} {self.surname} {self.second_name}"


class Score(Student):
    def __init__(self, name, surname, second_name, *score, **lesson_score):
        super().__init__(name, surname, second_name)
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
                return n*rec_fact(n-1)

        return rec_fact(number)


def main():
    secondname = os.getenv("NEW_VAR")

    student1 = Score("Sidorov", "Ivan", f"{secondname}", 5, 50, 30, math=100, baseball=1000)

    student1.name_func()
    student1.score_func()
    student1.factorial_class_func()


if __name__ == "__main__":
    main()
