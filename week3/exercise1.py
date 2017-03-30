# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""
from __future__ import division
from __future__ import print_function


def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from just using range()
    """
    list = []
    count = start
    while count < stop:
        list.append(count)
        count += step
    print(list)
    return list


def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    list = []
    count = start
    while count < stop:
        list.append(count)
        count += step
    print(list)
    return list


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    list = []
    step = 2
    count = start
    while count < stop:
        list.append(count)
        count += step
    print(list)
    return list


def gene_krupa_range(start, stop, even_step, odd_step):
    """Make a range that has two step sizes.

    make a list that instead of having evenly spaced steps
    has odd steps be one size and even steps be another.
    """
    list = []
    step = 2
    while start < stop:
        list.append(start)
        if step % 2:
            start += odd_step
            step += 1
        else:
            start += even_step
            step += 1
    print(list)
    return list


def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK
    """
    message = "Input a number between {low}, and {high}: ".format(low=low,
                                                                  high=high)

    while True:
        input_num = int(raw_input(message))
        if low < input_num < high:
            print("Thanks! {} looks good".format(input_num))
            return input_num
        else:
            print("Your input isnt within the bounds")


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number (e.g. "cow",
    "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    message = "Input a number"

    while True:
        try:
            input_num = int(raw_input(message))
            print("{} is a nice number".format(input_num))
            return input_num
        except Exception as e:
            print("That isn't a number...try again".format(e))


def super_asker(low, high):
    """Robust asking function.

    Combine stubborn_asker and not_number_rejector to make a function
    that does it all!
    """
    message = "Input a number between {low}, and {high}: ".format(low=low,
                                                                  high=high)

    while True:
        input_num = raw_input(message)
        try:
            input_num = int(input_num)
            if low < input_num < high:
                return input_num
            else:
                print("Your input isnt within the bounds")
        except Exception as e:
            print("That isn't a number...try again".format(e))

    return input_num


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from
    # inside Atom, you need to run them from the terminal. E.g.:
    # ben@um:~/projects/git/code1161base$ python week3/exercise1.py

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\ngene_krupa_range", gene_krupa_range(1, 20, 2, 5))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector()
    print("\nsuper_asker")
    super_asker(33, 42)
