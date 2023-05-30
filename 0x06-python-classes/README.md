# 0x06. Python - Classes and Objects

In Python, classes and objects are key components of object-oriented programming (OOP). Let's explore classes and objects in more detail:

## Classes:

A class is a blueprint or a template for creating objects. It defines the structure and behavior that objects of that class will have.
You define a class using the class keyword, followed by the name of the class (by convention, class names are capitalized).

```Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}!")
```
## Objects

An object is an instance of a class. It represents a specific occurrence of the class.
When you create an object, it has its own set of attributes and can perform actions defined by the class's methods.
You create objects by calling the class as if it were a function, passing any required arguments.

```Python
# Creating objects of the Person class

person1 = Person("John", 25)
person2 = Person("Alice", 30)
```
