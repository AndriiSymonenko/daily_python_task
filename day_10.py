
# Write a function that always returns 5
# Sounds easy right? Just bear in mind that you can't use any of the following characters: 0123456789*+-/
# Good luck :)

def unusual_five():
    return len('IIIII')



# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

def give_len_word(word_str):
    words = word_str.split()
    shortest_length = len(words[0])
    for word in words[1:]:
        if len(word) < shortest_length:
            shortest_length = len(word)
    return shortest_length


# Write a function that returns a string in which firstname is swapped with last name.
# Example(Input --> Output)
# "john McClane" --> "McClane john"

def name_shuffler(str_):
    words = str_.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words


# You will be given an array and a limit value. You must check that all values in the array are below or equal to the limit value. If they are, return true. Else, return false.
# You can assume all values in the array are numbers.

def small_enough(array, limit):
    bool = False
    for i in array:
        if i > limit:
            bool = False
            break
        else:
            bool = True
    return bool
