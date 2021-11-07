# Selection Sort - Print state of the array after x steps

def state_after_iterations(arr_list, N, x):
    for i in range(N):
        min_index = i    # Starting with min_index at 0th position
        for j in range(i+1, N):
            if arr_list[min_index] > arr_list[j]:
                min_index = j
        # Swap the found minimum element with the first element        
        arr_list[min_index], arr_list[i] = arr_list[i], arr_list[min_index]
        x -= 1

        # Break out of loop, if x steps completed
        if x == 0:
            break
    return arr_list


if __name__ == "__main__":
    N, x = map(int, input().split())
    arr_list = list(map(int, input().split()))
    for item in state_after_iterations(arr_list, N, x):
        print(item, end = " ")
    
    # N, x = 5, 2
    # arr_list = [1,2,3,4,5]
    # print(state_after_iterations(arr_list, N))