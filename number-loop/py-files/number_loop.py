# **************************** Challenge: Number Loop ****************************
"""
Author: Trinity Terry
pyrun: python number_loop.py
"""
# Write three functions that compute the sum of the numbers in a list: using a for-loop, a while-loop and recursion.

def for_sum(num_list):
    '''
    Sums Numbers using For Loop

    num_list - list of numbers

    Returns: Int
    '''
    sum = 0
    for num in num_list:
        if type(num) != int:
            raise TypeError("for_sum only accepts a list of numbers")
        
        sum += num
    
    return sum

def while_sum(num_list):
    '''
    Sums Numbers using While Loop

    num_list - list of numbers

    Returns: Int
    '''
    i = 0
    sum = 0
    while i < len(num_list):
        if type(num_list[i]) != int:
            raise TypeError("while_sum only accepts a list of numbers")
        sum += num_list[i]
        i += 1
    
    return sum


def recursion_sum(num_list, sum = 0, i = 0):
    '''
    Sums Numbers using Recursion Loop

    num_list - list of numbers

    Returns: Int
    '''
    number = sum
    if type(num_list) == list:
        if len(num_list) == i:
            return sum
        else:
            sum += num_list[i]
            i += 1

            # In recursive funtions you must return function call!!!
            return recursion_sum(num_list, sum, i)
            
        


print(for_sum([3, 6, 9, 1]))
print(while_sum([3, 6, 9, 1]))
print(recursion_sum([3, 6, 9, 1]))