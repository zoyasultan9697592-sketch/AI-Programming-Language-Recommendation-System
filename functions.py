from colorama import Fore
import time


def typing_effect(text, color=Fore.WHITE, delay=0.03):
    for char in text:
        print(color + char, end="", flush=True)
        time.sleep(delay)
    print()


def loading_animation():

    spinner = ["◐","◓","◑","◒"]

    for i in range(20):
        print("\rAnalyzing " + spinner[i % 4], end="")
        time.sleep(0.1)

    print()