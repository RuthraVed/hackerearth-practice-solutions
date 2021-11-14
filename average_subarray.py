# Average Subarray

# A solution from author of the problem - it's just O(n)
def authors_average_subarray(arr, N, K):
    sum_bits = ans = 0
    for current_value in arr:
        # If current value is 1.
        if current_value == "1":
            sum_bits += 1
            
            # If sum of bits is equal to K, 
            # it is same a finding average of sum for K bits.
            if sum_bits == K:
                ans += 1
                sum_bits = 0    # Reset sum_bits
        else:
            # Else if current value is not 1.
            sum_bits = 0 # Reset sum_bits
    return ans

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
            print(authors_average_subarray(input_list, N, K))
    # ----------------------------------------------------------
    """

    # HackerEarth Platform Input
    # ----------------------------------------------------------
    T = int(input())
    for i in range(T):
        N, K = map(int, input().split())
        input_list = input().split()
        print(authors_average_subarray(input_list, N, K))
    
