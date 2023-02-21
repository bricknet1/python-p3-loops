#!/usr/bin/env python3

def happy_new_year():
    for i in range(10,0,-1):
        print(i)
    print("Happy New Year!")

def square_integers(int_list):
    return [i ** 2 for i in int_list]

def fizzbuzz():
    for i in range(1,101):
        if (((i/3).is_integer()) and ((i/5).is_integer())):
            print("FizzBuzz")
        elif (i/5).is_integer():
            print("Buzz")
        elif (i/3).is_integer():
            print("Fizz")
        else:
            print(i)