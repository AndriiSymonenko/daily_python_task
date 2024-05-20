
def do_camel(string):
    for l in string:
        if l.upper() == l:
            index = string.index(l)
            result = string[:index] + string[index::]
            return result


# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing
# in this way until a single-digit number is produced. The input will be a non-negative integer.
def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n



# Create a method that will remove all characters in a string unless they are a letter.
def is_letter(text):
    string = []
    for el in text:
        if el.isalpha():
            string.append(el)
    return ''.join(string)


