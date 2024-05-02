def min_number(x, y):
    if x < y:
        return x
    else:
        return y


print(min_number(6, 3))


def is_leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return "YES"
    else:
        return "NO"


def min_three_num(x, y, z):
    if x < y and x < z:
        return x
    elif y < x and y < z:
        return y
    else:
        return z


def min_three_num_true(x, y, z):
    numbers = [x, y, z]
    min_num = numbers[0]  # Initialize min_num with the first number
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num


def count_matching_numbers(x, y, z):
    if x == y == z:
        return 3
    elif x == y or x == z or y == z:
        return 2
    else:
        return 0


def can_break_chocolate(n, m, k):
    area = n * m
    min_piece = n
    max_piece = area - n
    if min_piece <= k <= max_piece and (k % n == 0 or k % m == 0):
        return "YES"
    else:
        return "NO"
