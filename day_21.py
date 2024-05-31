
# Create a function to convert a list of percentages to their decimal equivalents.
def convert_to_decimal(perc):
    return [int(i.replace('%', '')) / 100 for i in perc]



# Write a function that moves all capital letters to the beginning of a word - a string.
def cap_to_front(word):
    upper_case = [char for char in word if char.isupper()]
    lower_case = [char for char in word if char.islower()]
    return ''.join(upper_case + lower_case)


