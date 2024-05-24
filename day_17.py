# print(date[-5:])
# The task is to create a function that takes a date in yyyy/mm/dd format
# as input and returns "Bonfire toffee" if the date is October 31, otherwise returns "toffee".
def halloween_day(date):
    if date[-5:] == '10/31':
        return 'Bonfire toffee'
    else:
        return 'toffee'



# The "reverser" takes a string and returns the same string
# with the letters in reverse order and with the case changed.
def reverser(string):
    res = []
    for char in string:
        if char == char.upper():
            res.append(char.lower())
        elif char == char.lower():
            res.append(char.upper())
    return ''.join(res[::-1])



#Write a function that takes a string and returns the leftmost digit in it.
def left_digit(string):
    for num in string:
        if num.isdigit():
            return num



# Write a function that takes an array of numbers and returns the median of a series of these numbers.
def median(number_list):
    number_list.sort()
    num = 0
    if len(number_list) % 2 != 0:
        num = len(number_list) // 2
        return number_list[num]
    else:
        num_1 = (len(number_list) // 2)
        num_2 = (len(number_list) // 2 - 1)
        return number_list[num_1] + number_list[num_2]
