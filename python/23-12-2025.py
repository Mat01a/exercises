"""
Exercise no. 1
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

"""


# O(n^2)
def check_k(k, bunch_of_numbers):
    for number in bunch_of_numbers:
        for current in range(len(bunch_of_numbers)):
            if number == bunch_of_numbers[current]:
                continue
            if bunch_of_numbers[current] + number == k:
                return True
        bunch_of_numbers.pop(0)
    return False


# O(n)
def check_sum(k, bunch_of_numbers):
    for number in range(len(bunch_of_numbers)):
        try:
            numbers_except_current = bunch_of_numbers[:]
            del numbers_except_current[number]
            if k - bunch_of_numbers[number] in numbers_except_current:
                return True
        except:
            continue
    return False

print(check_k(10, [2, 6, 5, 7]))
print(check_k(10, [10, 15, 3, 7]))
print(check_k(10, [2, 6, 4, 7]))

print(check_sum(10, [2, 6, 5, 7]))
print(check_sum(10, [10, 15, 3, 7]))
print(check_sum(10, [2, 6, 4, 7]))

