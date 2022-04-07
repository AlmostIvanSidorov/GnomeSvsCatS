from Packages import MyModule


def func():
    print("some func here")


if __name__ == '__main__':
    # SCRIPT HERE!!!

    print("my. program started directly")
    MyModule.my_func()
    func()
