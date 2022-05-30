from ipywidgets import interact,interactive,fixed
import ipywidgets as widgets


def func(x):
    return x


def main():
    # interact(func,x=10)
    widgets.IntSlider()


if __name__ == "__main__":
    main()
