
# Create a function with two arguments that will return an array of the first n multiples of x.
# Assume both the given number and the number of times to count will be positive numbers greater than 0.
# Return the results as an array or list
def count_by(x, n):
    return [i * x for i in range(1, n + 1)]


# Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each.
# If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.
# Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.
def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 != 0 or flower1 % 2 != 0 and flower2 % 2 == 0:
        return True
    else:
        return False


def has_spaces(txt):
    for char in txt:
        if char == ' ':
            return True
    return False
