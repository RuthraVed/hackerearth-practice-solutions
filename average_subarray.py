# Average Subarray

# This is my version of solution - it's O(n^2)
# Using Code Snippet: sub_arrays_v1
def my_average_subarray(arr, N, K):
    count = 0
    for i in range(N - (K - 1)):
        sum = 0
        for j in range(i, i + K):
            if arr[j] == "1":
                sum += 1
        # Check if average sum of bits is 1,
        # after inner-loop completes
        if sum == K:
            # Flipping last bit in the K subarray
            arr[(i+K)-1] = "0"
            i = (i+K) + 1 # Taking a leap forward to (K+1)th position
            count += 1
    return count


if __name__ == "__main__":

    """
    # Reading large inputs from file
    # ----------------------------------------------------------
    from pathlib import Path

    file_name = Path(__file__).stem + ".txt"
    input_file_path = Path().cwd() / r'large_input_files' / file_name
    print(f'Reading input from file at {input_file_path}.')
    with open(input_file_path, "r", encoding="utf8") as txt_file:
        T = int(txt_file.readline())
        for i in range(T):
            N, K = map(int, txt_file.readline().split())
            input_list = txt_file.readline().split()
            print(my_average_subarray(input_list, N, K))
    # ----------------------------------------------------------
    """

    # HackerEarth Platform Input
    # ----------------------------------------------------------
    T = int(input())
    for i in range(T):
        N, K = map(int, input().split())
        input_list = input().split()
        print(my_average_subarray(input_list, N, K))
    
