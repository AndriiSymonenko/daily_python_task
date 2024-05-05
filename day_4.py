
# Given a 2D ( nested ) list ( array, vector, .. ) of size m * n,
# your task is to find the sum of the minimum values in each row.

#For Example:

# [ [ 1, 2, 3, 4, 5 ]        #  minimum value of row is 1
# , [ 5, 6, 7, 8, 9 ]        #  minimum value of row is 5
# , [ 20, 21, 34, 56, 100 ]  #  minimum value of row is 20
# ]

def get_min_2d_list (test_list):
    result = 0
    for item in test_list:
        result += min(item)
    return result



# In this simple assignment you are given a number and have to make it negative.
# But maybe the number is already negative?

# The number can be negative already, in which case no change is required.
# Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.

def make_negative(number):
    if number < 0:
        return number
    else:
        number *= -1
        return number


# Write a function to split a string and convert it into an array of words.
# Examples (Input ==> Output):

# "Robin Singh" ==> ["Robin", "Singh"]
# "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]

def string_to_array(string):
    return string.split(" ")



# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:
# Sam Harris => S.H
# patrick feeney => P.F

def abbrev_name(name):
    initials = name.split()
    name_list = initials[0][0], initials[1][0]
    lower_name = '.'.join(name_list)
    return lower_name.upper()

