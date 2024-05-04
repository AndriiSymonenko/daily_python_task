# Given an array of numbers, return a new array of length number containing the last even numbers from the original
# array (in the same order). The original array will be not empty and will contain at least "number" even numbers.

def calc_last_even_in_list(number_list, even_number_quantity):
    even = []
    for i in number_list:
        if i % 2 == 0:
            even.append(i)
    return even[-even_number_quantity:]


int_list = [6, 2, 3, 4, 5, 6, 7, 8, 9]
int_list_2 = [6, -25, 3, 7, 5, 5, 7, -3, 23]
int_list_3 = [-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26]

print(calc_last_even_in_list(int_list, 4))

print(calc_last_even_in_list(int_list_2, 1))


# Given a non-negative integer, return an array / a list of the individual digits in order.
# Examples:
# 123 => [1,2,3]
# 1 => [1]
# 8675309 => [8,6,7,5,3,0,9]

def digit_to_list(num):
    digit_list = list(str(num))
    num_list = []
    for i in digit_list:
        num_list.append(int(i))
    return num_list


digit = 13453252
print(digit_to_list(digit))


def digit_to_list_v2(num):
    num_list = []

    while num > 0:
        digit = num % 10
        num //= 10
        num_list.insert(0, digit)

    return num_list


print(digit_to_list_v2(digit))


# You are going to be given a word.
# Your job is to return the middle character of the word. If the word('s length is odd, return the middle character.'
# If the word')s length is even, return the middle 2 characters.

#Examples:
# Kata.get_Middle("test") should return "es"
# Kata.get_Middle("testing") should return "t"
# Kata.get_Middle("middle") should return "dd"
# Kata.get_Middle("A") should return "A"

def get_Middle(string):
    mid = int(len(string) // 2)
    if len(string) % 2 == 0:
        print(string[mid - 1], string[mid])
    else:
        print(string[mid])
