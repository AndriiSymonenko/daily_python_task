
# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.
# Array can contain numbers or strings. X can be either.
# Return true if the array contains the value, false if not.

def check(seq, elem):
    for i in seq:
        if i == elem:
            return True
    else:
        return False

def check_var_two(seq, elem):
    return elem in seq


# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"

def high_and_low(numbers):
    num_list = [int(num) for num in numbers.split()]
    max_min = max(num_list), min(num_list)
    max_min_str = [str(num) for num in max_min]
    result = ' '.join(max_min_str)
    return result
# Write a function that checks if a given string (case insensitive) is a palindrome.
# A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as madam or racecar.

def palindrome(word):
    return word[::-1].lower() == word.lower()