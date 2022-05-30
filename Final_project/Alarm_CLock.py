"""
A simple clock where it plays a sound after X number of minutes/seconds or at a particular time
"""

import time
from pygame import mixer


def alarm_beep():
    mixer.init()
    sound = mixer.Sound("StarWars3.wav")
    sound.play()


def alarm(n):
    print(f"Wait {n} seconds and BEEEEEP")
    time.sleep(n)
    alarm_beep()


def main():
    """Alarm second timer"""
    print("Welcome to Alarm Second Timer")
    while True:
        user_seconds = input("Please enter some integer value of seconds for timer or 'quit' command:")
        if user_seconds == 'quit':
            break
        if not user_seconds.isdigit():
            print("Please enter an integer value")
        else:
            alarm(int(user_seconds))


if __name__ == "__main__":
    main()

