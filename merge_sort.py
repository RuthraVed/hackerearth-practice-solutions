# Python program for implementation of MergeSort

# Merge Sort Algorithm
def mergeSort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr)//2
        
        # Divide...
        # The array elements into
        L, R = arr[:mid], arr[mid:]   # A Left half & A Right half
        mergeSort(L)
        mergeSort(R)
        
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
    arr = [100, 99, 88]
    
    # Code to print the list
    def printList(arr):
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()
    
    print("Given array is", end="\n")
    printList(arr)
    
    mergeSort(arr)
    
    print("Sorted array is: ", end="\n")
    printList(arr)

# This code is contributed by Abhishek Dev
