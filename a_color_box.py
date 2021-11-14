# A Color Box

# Problem setter's logic
def color_buckets_possible(N, A_list, B_list):
    have_buckets = 0
    required_buckets = 0
    for i in range(N):
        if A_list[i] == B_list[i]:
            continue
        if A_list[i] > B_list[i]:
            have_buckets += (A_list[i] - B_list[i])//2
        elif B_list[i] > A_list[i]:
            required_buckets += B_list[i] - A_list[i]
    
    if have_buckets >= required_buckets:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":

    """
    # HackerEarth Platform Input
    # ----------------------------------------------------------
    T = int(input())
    for i in range(T):
        N = int(input())
        bobs_bucket_list = list(map(int, input().split()))
        min_bucket_list = list(map(int, input().split()))
        color_buckets_possible(N, bobs_bucket_list, min_bucket_list)
    # ----------------------------------------------------------
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
            N = int(txt_file.readline())
            bobs_bucket_list = list(map(int, txt_file.readline().split()))
            min_bucket_list = list(map(int, txt_file.readline().split()))
            color_buckets_possible(N, bobs_bucket_list, min_bucket_list)
    # ----------------------------------------------------------
