

# A number is given. Print the number of digits in this number.
def num_of_digits(num):
    num_str = str(num)
    return len(num_str)


# Complete the square sum function so that it squares each number passed into it and then sums the results together.
def square_sum(numbers):
    result = 0
    for i in numbers:
        num = i ** 2
        result += num
    return result


# Write a function which takes a number and returns the corresponding ASCII char for that value.
def get_char(c):
    try:
        return chr(c)
    except ValueError:
        return "Invalid ASCII code"


#Round the list of fractions to one decimal place.
def round_num(list_num):
    list_num = [round(i, 1) for i in list_num]
    return list_num

