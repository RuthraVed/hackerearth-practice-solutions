# Bubble Sort - Counting number swaps

def count_swaps(arr, N):
    swap_counter = 0
    # Traverse through all array elements
    # range(N) also works but in that case outer loop will repeat one time more than needed.
    for i in range(N):
        # Last i elements are already in place
        for j in range((N-1)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_counter += 1
    return swap_counter


if __name__ == "__main__":
    N = int(input())
    unsorted_input = list(map(int, input().split()))
    print(count_swaps(unsorted_input, N))