#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Happy New Year!")

    # code goes here!
    pass

def square_integers(int_list):
    squared = []
    for num in int_list:
        squared.append(num ** 2)
    return squared

    # code goes here!
    pass

def fizzbuzz():
    num = 1
    while num <= 100:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
        num += 1
    # code goes here!
    pass
