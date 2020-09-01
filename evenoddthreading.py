# this program is made using the threadings in python
# the concept of threading is bascially running two threads simultaneously
# one thread wait while otner one is completed
import threading as th
import time


even_event = th.Event()
odd_event = th.Event()


def even_function():
    for i in range(0, 30, 2):
        print(i)
        odd_event.set()
        even_event.clear()
        even_event.wait()
    return


def odd_function():
    odd_event.wait()
    for i in range(1, 30, 1):
        print(i)
        even_event.set()
        odd_event.clear()
        odd_event.wait()
    return


odd_function()
even_function()
