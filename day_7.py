# Make a program that filters a list of strings and returns a list with only your friends name in it.
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
# friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]

def filter_friends(names):
    friends = []
    for name in names:
        if len(name) == 4:
            friends.append(name)
    return friends


# Given a non-empty array of integers, return the result of multiplying the values together in order.

def grow(arr):
    product = 1
    for i in arr:
        product *= i
    return product


#
# Given an array of integers, return a new array with each value doubled.

def maps(a):
    product_arr = []
    for i in a:
        i *= 2
    product_arr.append(i)
    return product_arr


# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

def digitize(n):
    digits = [int(digit) for digit in str(n)]
    return digits[::-1]


# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.

def delete_vowel(string_):
    vowels = 'aeiouAEIOU'
    string_ = ''.join([char for char in string_ if char not in vowels])
    return string_
