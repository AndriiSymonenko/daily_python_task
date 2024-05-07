# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
# Return your answer as a number.

def sum_mix(test):
    result = 0
    for el in test:
        if int(el):
            n_el = int(el)
            result += n_el
    return result


# You get an array of numbers, return the sum of all of the positives ones.
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
# Note: if there is nothing to sum, the sum is default to 0.
def sum_positive(lst):
    result = 0
    for num in lst:
        if num > 0:
            result += num
    return result


# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
# Examples:
# ('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def solution(text, ending):
    if text[- len(ending):] == ending:
        return True
    else:
        return False


def solution_var_two(text, ending):
    return text.endswith(ending)


# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.
# If the input is an empty array or is null, return an empty array.
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

def num_counter(arr):
    if arr is None or len(arr) == 0:
        return []
    positive_count = sum_negative = 0

    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            sum_negative += num

    return [positive_count, sum_negative]


# Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.
# Examples (input -> output)
# 6, "I"     -> "IIIIII"
# 5, "Hello" -> "HelloHelloHelloHelloHello"

def repeat_str(repeat, string):
    return string * repeat
