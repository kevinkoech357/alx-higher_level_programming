# 0x07. Python - Test-driven development
TDD (Test-Driven Development) is a software development approach that emphasizes writing tests before writing the actual code. The process involves writing a failing test, writing the minimum code required to make the test pass, and then refactoring the code as necessary while ensuring all tests continue to pass. TDD helps in improving code quality, maintainability, and ensures that the code meets the desired requirements.

To practice TDD in Python, you can follow these steps:

Write a test: Start by writing a test that describes the behavior you want to implement. A test typically consists of assertions that verify the expected behavior of your code. Use a testing framework like unittest, pytest, or doctest to define and run tests.

For example, let's say you want to create a function that adds two numbers:

```python
import unittest

def add_numbers(a, b):
    return a + b

class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)
```		
Run the test: Run the test and see it fail. This step ensures that the test is valid and correctly identifies the missing functionality.

When using unittest, you can run the tests from the command line using a test runner such as python -m unittest <test_module>.

Implement the code: Write the minimum amount of code necessary to make the test pass. Avoid adding unnecessary functionality at this stage.

```python
def add_numbers(a, b):
    return a + b
```
Run the test again: Run the test suite again to ensure that the newly added code passes the test. If the test fails, iterate on the implementation until it passes.

Refactor: Once the test passes, you can refactor the code to improve its design, readability, and performance. Refactoring should not change the behavior of the code without corresponding changes in the tests.

Refactoring example:

```python
def add_numbers(a, b):
    return a + b
```	
Write additional tests: Write additional tests to cover different scenarios and edge cases. This helps ensure that your code is robust and handles various inputs correctly.

```python
class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_add_numbers_negative(self):
        result = add_numbers(-2, 3)
        self.assertEqual(result, 1)
```
Repeat the process: Repeat the steps for each new feature or behavior you want to add, ensuring that you always write tests first and follow the red-green-refactor cycle.

By following the TDD process, you can gradually build a suite of tests that provide confidence in the correctness of your code while maintaining the ability to refactor and modify it as needed.





