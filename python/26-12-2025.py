"""
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

# O(2n+1)
def first_excluded_number(numbers):
    lowest_number = min(n for n in numbers if n > 0)
    while True:
        if lowest_number + 1 not in numbers:
            return lowest_number + 1
        lowest_number += 1

# O(n)
def find_first_positive_number(numbers):
    first_lowest = max(numbers)+1
    for each in numbers:
        if each <= 0:
            continue
        if each+1 < first_lowest and each+1 not in numbers:
            first_lowest = each+1
    return first_lowest
a = [3,4,-1,1]
b = [1, 2, 0]

assert find_first_positive_number(a) == 2
assert find_first_positive_number(b) == 3
