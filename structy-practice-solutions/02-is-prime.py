"""
    ## Is Prime ##

    Write a function, is_prime, that takes in a number as an argument. 
    The function should return a boolean indicating whether or not the given number is prime.

    A prime number is a number that is only divisible by two distinct numbers: 1 and itself.
    For example, 7 is a prime because it is only divisible by 1 and 7. For example, 6 is not a prime 
    because it is divisible by 1, 2, 3, and 6.

    You can assume that the input number is a positive integer.

"""

from timer_module import timer_func
from math import sqrt, floor

# --- Solution ---
@timer_func
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, floor(sqrt(n))+1):
        if n % i == 0:
            return False

    return True


# --- Tests --- 

test_input_values = [
    2, 3, 5, 6, 
    7, 8, 25, 31,
    2017, 2048, 1, 713,
]

expected_results = [
    True, True, True, False,
    True, False, False, True,
    True, False, False, False,
]

for i in range(0,len(test_input_values)):
    result = is_prime(test_input_values[i])    # Test solution against every input
    assert result == expected_results[i], \
        f'Expected max value as {expected_results[i]}, got: {result}'
    print(f'test [{i}] passed, with correct result as {expected_results[i]}.')
