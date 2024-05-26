
# Write a function that converts a date in DD/MM/YYYY format to YYYYMMDD.
def convert_date(string):
    date = string[6:] + string[3:5] + string[0:2]
    return date




# ATMs allow 4 or 6 digit PINs, and PINs cannot contain anything other than exactly
# 4 or exactly 6 digits. Your task is to create a function that takes a string and
# returns True if the PIN is valid and False if it is invalid.
def is_valid_PIN(pin):
    if len(pin) > 4:
        return False
    for i in pin:
        if not i.isdigit():
            return False
    else:
        return True



# Create a function that accepts a string and a single character,
# and returns an integer of the count of occurrences the 2nd argument is found in the first one.
# If no occurrences can be found, a count of 0 should be returned.
def str_count(strng, letter):
    count = 0
    for i in strng:
        if i == letter:
            count += 1
    return count

