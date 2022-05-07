"""
    ## Uncompress ##
    Write a function, uncompress, that takes in a string as an argument.
    The input string will be formatted into multiple groups
    according to the following pattern:

    <number><char>

    For example, '2c' or '3a'.
    The function should return an uncompressed version of the string 
    where each 'char' of a group is repeated 'number' times consecutively, 
    like 'ccc' or 'aaa'.
    
    You may assume that the input string is well-formed according to the previously mentioned pattern.

"""

from timer_module import timer_func

@timer_func
def uncompress(s):
    number_str = ''
    uncompressed_result = ''
    for char in s:
        if char.isdigit():
            # Keep saving the consecutive digits as string
            number_str += char
        else:
            uncompressed_result += char*int(number_str)
            # Reinitialize to store a new number
            number_str = ''
    
    return uncompressed_result

# --- Tests --- 

test_input_values = [
    "2c3a1t",
    "4s2b",
    "2p1o5p",
    "3n12e2z",
    "127y",
]

expected_results = [
    'ccaaat',
    'ssssbb',
    'ppoppppp',
    'nnneeeeeeeeeeeezz',
    'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy',
]

for i in range(0,len(test_input_values)):
    result = uncompress(test_input_values[i])    # Test solution against every input
    assert result == expected_results[i], \
        f'Expected max value as {expected_results[i]}, got: {result}'
    print(f'test [{i}] passed, with correct result as {expected_results[i]}.')
