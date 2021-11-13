# Python program for implementation of MergeSort

# Implementation of Merge Sort Algorithm
def merge_sort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2

        # Divide...
        # The array elements into
        L, R = arr[:mid], arr[mid:]  # A Left half & A Right half
        merge_sort(L)
        merge_sort(R)

        # Conquer...
        # By sorting and merging the two parts into one
        merge(arr, L, R)


# Merge Sort's sorting & merging function
def merge(arr, L, R):
    i = j = k = 0

    # To place larger among elements L and R,in the correct position
    # until we reach either end of either L or R,
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # To put remaining elements in the merged list, as they are...
    # When left side remains
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    # When right side remains
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


# Driver Code
if __name__ == '__main__':

    # Reading large inputs from file
    # ----------------------------------------------------------
    from pathlib import Path

    file_name = Path(__file__).stem + ".txt"
    input_file_path = Path().cwd() / r'large_inputs' / file_name
    print(f'Reading input from file at {input_file_path}.')
    with open(input_file_path, "r", encoding="utf8") as txt_file:
        arr_list = list(map(int, txt_file.readline().split()))
    # ----------------------------------------------------------

    # Code to print the list
    def print_list(arr):
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()

    merge_sort(arr_list)  # Merge Sort Call
    print("Sorted array is: ", end="\n")
    print_list(arr_list)

# This code is contributed by Abhishek Dev
