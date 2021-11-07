# Insertion Sort - Give position of the indices, as if array were sorted.

def insertion_sort(arr, N):
    for i in range(1, N):
        key = arr[i]
        j = i - 1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]   # Shifting the elements to the right, until they are greater than the key
            j -= 1
        arr[j+1] = key  # Finally setting key value to a position, from where key was no longer smallest. 

    return arr

if __name__ == "__main__":
    N = int(input())
    input_arr = list(map(int, input().split()))
    original_arr = input_arr[:] # Replicating the input_arr, to save unsorted array
    sorted_arr = insertion_sort(input_arr, N)   # Function call
    for item in original_arr:
        print(sorted_arr.index(item)+1, end = " ")
