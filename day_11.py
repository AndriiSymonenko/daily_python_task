# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []

def invert(lst):
    return [int * -1 for int in lst]


num = []


# def remove_smallest(numbers):
#     min_arr = numbers
#     min_arr.remove(min(min_arr))
#     return min_arr

# Given an array of integers, remove the smallest value. Do not mutate the original array/list.
# If there are multiple elements with the same value, remove the one with the lowest index.
# If you get an empty array/list, return an empty array/list.
# Don't change the order of the elements that are left.
# Examples
# * Input: [1,2,3,4,5], output = [2,3,4,5]
# * Input: [5,3,2,1,4], output = [5,3,2,4]
# * Input: [2,2,1,2,1], output = [2,2,2,1]

def remove_smallest(arr):
    if not arr:
        return []
    min_index = arr.index(min(arr))
    new_arr = arr[:min_index] + arr[min_index + 1:]
    return new_arr


#This time no story, no theory. The examples below show you how to write function accum:
#Examples:
#accum("abcd") -> "A-Bb-Ccc-Dddd"
#accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(st):
    result_parts = []
    for i, char in enumerate(st):
        result_parts.append((char.upper() + char.lower() * i))

    return '-'.join(result_parts)


