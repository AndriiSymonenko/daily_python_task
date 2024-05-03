def last_digit(number):
    return number % 10

number = 12
print("Last digit of the number", number, ":", last_digit(number))


def calculate_cost_pie(a, b, n):
    total_cost_in_kop = (a * 100 + b) * n

    rubles = total_cost_in_kop // 100
    kop = total_cost_in_kop % 100
    return rubles, kop


def palindrome(word):
    if word[::-1] == word:
        return 'YES'
    else:
        return 'NO'


def even_odd(num_list):
    even = []
    odd = []
    for i in num_list:
        if i % 2 == 0:
            even.append(i)
        else:
           odd.append(i)
    print(*even)
    print(*odd)


#Variant_1

def sum_integer_list(string):
    new = string.replace(" ", "")
    char = []
    num = []
    for i in new:
        char.append(i)

    for n in char:
        if n.isdigit():
            num.append(int(n))
    result = sum(num)
    return result


#Variant_2
def sum_of_integers_in_string(string):
    current_number = 0
    total_sum = 0

    for char in string:
        if char.isdigit():
            current_number += int(char)
        else:
            total_sum += current_number
            current_number = 0

    total_sum += current_number

    return total_sum


s = "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"
result = sum_of_integers_in_string(s)
print("Sum of integers in the string:", result)
