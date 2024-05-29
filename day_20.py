
# Write a function that takes a list of elements and returns only integers.
def return_only_integer(lst):
    return [i for i in lst if isinstance(i, int)]


# Write a function that takes a word as a txt string and returns a string
# with the letters of the word rearranged in alphabetical order.
def alphabet_soup(txt):
    return ''.join(sorted(txt))


# Create a function that takes a list of numbers from 1 to 10 (excluding one number)
# and returns the missing number.
def missing_num(lst):
    test_lst = [i + 1 for i in range(10)]
    return list(set(test_lst) - set(lst))
