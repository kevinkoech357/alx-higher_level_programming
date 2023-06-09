#!/usr/bin/python3

"""
Unittest for max_integer function.
Prints the largest integer in a list.
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    A unittest for max_integer function.
    """
    def test_empty_list(self):
        """
        Testing an empty list
        """
        list = []
        self.assertEqual(max_integer(list), None)

    def test_sorted_list(self):
        """
        Testing a sorted list.
        """
        sorted_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(sorted_list), 4)

    def test_unsorted_list(self):
        """
        Testing an unsorted list.
        """
        unsorted_list = [4, 1, 3, 2]
        self.assertEqual(max_integer(unsorted_list), 4)

    def test_floats(self):
        """
        Testing a list of floats.
        """
        float_list = [1.1, 2.2, 3.3, 4.4]
        self.assertEqual(max_integer(float_list), 4.4)

    def test_negatives(self):
        """
        Testing negative values in a list.
        """
        negative_list = [-1, -2, -3, -4]
        self.assertEqual(max_integer(negative_list), -1)

if __name__ == "__main__":
    unittest.main()
