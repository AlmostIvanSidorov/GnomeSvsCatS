def decorator_func(original_func):
    def wrap_func():
        print("Actions before")
        original_func()
        print("Actions after")
    return wrap_func


@decorator_func
def func_need_decorator():
    print("I need to be decorated!")


def square_func(N):
    for number in range(N+1):
        yield number**2


if __name__ == '__main__':

    func_need_decorator()

    new_suare_func = square_func(5)

    for i in square_func(6):
        print(i)

