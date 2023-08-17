#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while counter >= 1: # i included 1 in the count down
        print ("counter")
        counter -= 1
    print("Happy New Year!")
    

def square_integers(int_list):
    return [num ** 2 for num in int_list]
    
    

def fizzbuzz():
    for num in range(1, 101):
        print(fizzbuzz_printer(num))

def fizzbuzz_printer(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"    
    elif num % 3 == 0:  
        return "Fizz"  
    elif num % 5 ==0:
        return "Buzz"
    else:
        return num

def reverse_string(s) :
    reversed_str = "" 
    for char in s: #initiates a loop that iterates over each character
        reversed_str = char + reversed_str #places current character infront of the already reversed portion of the string
    return reversed_str   

