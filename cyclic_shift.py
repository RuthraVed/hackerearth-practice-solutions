# Cyclic shift

def cyclic_shift(N, str_binary, K):

    temp_str_binary = str_binary
    max = temp_str_binary   # Assign to max an intial value, before making 1st shift.
    shift_count = 0         # A var to count number of shifts made.
    max_found_at_shift = 0  # A var to note the ith shift, at which max was found
    periodicity = 0         # A var to note if we may get the initial str_binary, before full N iterations.
    
    for i in range(N):
        temp_str_binary = temp_str_binary[1:] + temp_str_binary[:1]  # Cyclic Shifting to left by 1
        shift_count += 1
        if temp_str_binary > max:
            max = temp_str_binary
            max_found_at_shift  = shift_count
        if temp_str_binary == str_binary:
            periodicity = shift_count
            break

    result = max_found_at_shift + periodicity*(K-1)
    return result

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N, K = map(int, input().split())
        str_binary = input()
        print(cyclic_shift(N, str_binary, K))