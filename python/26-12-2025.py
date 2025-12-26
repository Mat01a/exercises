"""
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

# O(n+1)
def first_excluded_number(numbers):
    lowest_number = min(n for n in numbers if n > 0)
    while True:
        if lowest_number + 1 not in numbers:
            return lowest_number + 1
        lowest_number += 1

a = [3,4,-1,1]
b = [1, 2, 0]

