"""
    ## Max Value ##

    Write a function, max_value, that takes in list of numbers as an argument.
    The function should return the largest number in the list.

    Solve this without using any built-in list methods.
    You can assume that the list is non-empty.

"""
from time import time

# Defining a decorator to time execution of any fucntion
def timer_func(func):
    # This function shows the execution time of 
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'In {(t2-t1):.4f}s ', end="")
        return result
    return wrap_func


# --- Solution ---
@timer_func
def max_value(nums):
    max = float('-inf') # Assigned infinity as an initial value to 'max'
    for num in nums:
        if num > max:
            max = num

    return max


# --- Tests --- 

test_input_values = [
    [4, 7, 2, 8, 10, 9],
    [10, 5, 40, 40.3],
    [-5, -2, -1, -11],
    [42],
    [1000, 8],
    [1000, 8, 9000],
    [2, 5, 1, 1, 4],
]

expected_results = [
    10, 40.3, -1, 42, 1000, 9000, 5
]

for i in range(0,len(test_input_values)):
    result = max_value(test_input_values[i])
    assert result == expected_results[i], \
        f'Expected max value as {expected_results[i]}, got: {result}'
    print(f'test [{i}] passed, with correct result as {expected_results[i]}.')