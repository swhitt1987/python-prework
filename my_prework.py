# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print("hello_" + user_name.upper() +"!")

hello_name("USERNAME")

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for n in range(1, 100):
        if n % 2 == 1:
            print(n)
# Need to run first_odds to get the list to return

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    max_number = a_list[0]
    for number in a_list:
        if number > max_number:
            max_number = number
    return max_number
a_list = [5, 7, 12, 4, 8]
print(max_num_in_list(a_list))

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, 
# unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if a_year % 400 == 0:
        return True
    elif a_year % 100 == 0:
        return False
    elif a_year % 4 == 0:
        return True
    else:
        return False

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, 
# but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    sort_a_list = sorted(a_list)
    for number in range(1, len(sort_a_list)):
        if sort_a_list[number] != sort_a_list[number-1] + 1:
            return False
    else: 
        return True
