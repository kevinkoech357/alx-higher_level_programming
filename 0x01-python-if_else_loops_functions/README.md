# Python - if/else, loops, functions
This repository contains examples of using conditionals (if/else statements), loops (for and while loops), and functions in Python.

## Conditionals: if/else
The if/else statement allows you to execute different code depending on whether a condition is true or false. In Python, the syntax for an if/else statement is:

'''
if condition:
    # code to execute if condition is true
else:
    # code to execute if condition is false
'''

For example:
'''
x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
'''
Output:
'''
x is greater than 5
'''

## Loops: for and while
The for and while loops allow you to execute a block of code multiple times.

### for loop
The for loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable object. In Python, the syntax for a for loop is:

'''
for variable in sequence:
    # code to execute for each item in the sequence
'''
For example:
'''
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
'''
Output:
'''
apple
banana
cherry
'''

### while loop
The while loop is used to execute a block of code repeatedly as long as a condition is true. In Python, the syntax for a while loop is:
'''
while condition:
    # code to execute as long as the condition is true
'''
For example:
'''
i = 1

while i <= 5:
    print(i)
    i += 1
'''

Output:
'''
1
2
3
4
5
'''

## Functions
Functions are a way to break up code into reusable parts. In Python, a function is defined using the def keyword, followed by the function name and any parameters in parentheses. The code to be executed by the function is indented below the function definition.

'''
def function_name(parameter1, parameter2, ...):
    # code to execute when the function is called
    return result
'''
For example:

'''
def greet(name):
    print("Hello, " + name + "!")

greet(Kevin")
'''
Output:

'''
Hello, Kevin!
'''

