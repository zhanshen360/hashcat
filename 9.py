#!/usr/bin/python
# coding:utf-8
import random

value2_index = set(["1","2","9","8","4","A","B","D","E","F","G","J","K","L","M","P","R","S","T","W","Y"])
value2_index1 = set(["a","d","e","f","g","h","i","j","k","m","n","o","p","q","r","s","t","u","v","w","y","!","-"])
value2_index2 = set(["2","3","4","5","6","7","8","9","t","u","v","w","x","y","z","!","?","-"])
def function():
    while True:
        result = ""
        pick_from = value2_index
        for digit in range(1):
            cur_digit = random.sample(value2_index, 1)[0]
            result += cur_digit
            if result[-1] == cur_digit:
                pick_from = value2_index - set(cur_digit)
            else:
                pick_from = int(value2_index)
        yield result
        
def function1():
    while True:
        result1 = ""
        pick_from = value2_index1
        for digit in range(4):
            cur_digit = random.sample(value2_index1, 1)[0]
            result1 += cur_digit
            if result1[-1] == cur_digit:
                pick_from = value2_index1 - set(cur_digit)
            else:
                pick_from = int(value2_index1)
        yield result1

def function2():
    while True:
        result2 = ""
        pick_from = value2_index2
        for digit in range(4):
            cur_digit = random.sample(value2_index2, 1)[0]
            result2 += cur_digit
            if result2[-1] == cur_digit:
                pick_from = value2_index2 - set(cur_digit)
            else:
                pick_from = int(value2_index2)
        yield result2

my_function = function()
my_function1 = function1()
my_function2 = function2()
counter = 0

while True:
   counter += 1
   result = next(my_function)
   result1 = next(my_function1)
   result2 = next(my_function2)
   print(str(result)+str(result1)+str(result2))
   if counter > 40000000:
     break
