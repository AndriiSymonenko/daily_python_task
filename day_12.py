
# Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.
# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
# None of the arrays will be empty, so you don't have to worry about that!

def remove_every_other(my_list):
   return my_list[::2]




# Given a list of integers, determine whether the sum of its elements is odd or even.
# Give your answer as a string matching "odd" or "even".
# If the input array is empty consider it as: [0] (array with a zero).

def odd_or_even(arr):
   return 'even' if sum(arr) % 2 == 0 else 'odd'



# You are given two interior angles (in degrees) of a triangle.
# Write a function to return the 3rd.
# Note: only positive integers will be tested.

def other_angle(a, b):
   return 180 - (a + b)




# After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.
# You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.
# Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.
# Write a code that gives out the total amount for different days(d).

def rental_car_cost(d):
   if d < 3:
      return d * 40
   elif 3 < d < 7:
      return d * 40 - 20
   elif d >= 7:
      return d * 40 - 50




