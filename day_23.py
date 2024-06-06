# Your task, is to create N×N multiplication table, of size provided in parameter.
def multiplication_table(size):
    return [[(i + 1) * (j + 1) for j in range(size)] for i in range(size)]





# You are given an array (which will have a length of at least 3, but could be very large) containing integers.
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
# Write a method that takes the array as an argument and returns this "outlier" N.
def find_outlier(arr):
    sample = arr[:3]
    even_count = sum(1 for x in sample if x % 2 == 0)

    if even_count >= 2:
        for num in arr:
            if num % 2 != 0:
                return num
    else:
        for num in arr:
            if num % 2 == 0:
                return num