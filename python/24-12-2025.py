import math

"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

"""

# O(n)
def product_of_remaining_numbers(numbers):
    new_set_of_numbers = numbers[:]
    for i in range(len(numbers)):
        product = numbers[:]
        del product[i]

        sum_of_products = math.prod(product)
        new_set_of_numbers = numbers[i] * sum_of_products
    return new_set_of_numbers

print(product_of_remaining_numbers([1, 2, 3, 4, 5]))


