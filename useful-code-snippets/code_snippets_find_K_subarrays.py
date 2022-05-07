# Code Snippets: To find K sub array in araay N items

def sub_arrays_v1(arr, K):
    count = 0
    N = len(arr)
    # From i=0 till N with K steps less.
    # This is to avoid index out-of-bound error in inner loop
    for i in range(N - (K - 1)):
        # From j=i till K steps
        for j in range(i, i + K):
            print(arr[j], end=" ")
        count += 1
        print()
    return f'A total of {count} sub-arrays found.\n'


def sub_arrays_v2(arr, K):
    count = 0
    N = len(arr)
    for i in range(0, N - 1):
        print(arr[i:i + K])
        count += 1
    return f'A total of {count} sub-arrays found.\n'


input_list = [1, 0, 1, 1, 4]
print(sub_arrays_v1(input_list, 2))
print(sub_arrays_v2(input_list, 2))
