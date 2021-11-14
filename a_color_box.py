# A Color Box

# My initial logic
def color_buckets_possible(N, bobs_bucket_list, min_bucket_list):
    excess_buckets_count = 0
    for i in range(len(bobs_bucket_list)):
        extra_buckets = (bobs_bucket_list[i] - min_bucket_list[i])//2
        if extra_buckets >= 0:
            excess_buckets_count += extra_buckets
        else:
            excess_buckets_count += extra_buckets

    if excess_buckets_count >= 0:
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
