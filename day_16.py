
#Count how many times a character appears in a line.
def char_count(sentence, char):
    count = [i for i in sentence if char == i]
    return len(count)


# Write a function change(lst) that takes a list and swaps its first and last elements.
# The original list has at least 2 elements.
def change_list(lst):
    lst[0], lst[len(lst) - 1] = lst[len(lst) - 1], lst[0]
    return lst


# The task is to create a recursive function that takes two
# parameters and repeats a string n times.
# The first parameter txt is the line to be repeated, and
# the second parameter is the number of times the line will be repeated.
def repeat_string(string, repeat):
    for i in range(1, repeat + 1):
        print(string)


# Write a function that returns the number of syllables in the given string.
# The line consists of short repeated words. For example, the line "Lalalalalalala" has 7 syllables.
def syllable_count(string):
    return string.count('a')

# The problem is to measure the depth of a list where []
# has depth 1, [[]] has depth 2, [[[]]] has depth 3, and so on.
def deep_list(lst):
    return str(lst).count('[')

