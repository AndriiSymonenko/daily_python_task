
# Build a function that returns an array of integers from n to 1 where n>0.
# Example : n=5 --> [5,4,3,2,1]

def reverse_seq(n):
    num = []
    while n > 0:
        num.append(n)
        n -= 1
    return num


# Create a method to see whether the string is ALL CAPS.
def is_uppercase(inp):
    return (inp.upper() == inp)


# Complete the function/method so that it returns the url with anything after the anchor (#) removed.
def remove_after_character(input_string):
    index = input_string.find('#')
    if index != -1:
        return input_string[:index]
    else:
        return input_string


def remove_after_character_var2(input_string):
         return input_string.split('#')[0]

