# Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java
def get_extension(string):
    return string[(string.find('.') + 1):]


# Write a function that creates a combination of two lists like this:
# [1, 2, 3] (+) [11, 22, 33] -> [1, 11, 2, 22, 3, 33]
def concat_list(lst_1, lst_2):
    count = 1
    for i in lst_2:
        lst_1.insert(count, i)
        count += 2
    return lst_1


# Write a function which removes from string all non-digit characters and parse the remaining to number. E.g: "hell5o wor6ld" -> 56
def get_number_from_string(st):
   temp_list = [i for i in st if i.isdigit()]
   return int(''.join(temp_list))

