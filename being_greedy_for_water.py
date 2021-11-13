# Being greedy for Water

def max_bottles_filled(sorted_bottle_list, container_capacity):
    bottles_filled = 0
    for bottle_capacity in sorted_bottle_list:
        container_capacity = container_capacity - bottle_capacity
        if container_capacity > 0:
            bottles_filled += 1
        else:
            break
    return bottles_filled


# Driver Code
if __name__ == '__main__':

    # Reading large inputs from file
    # ----------------------------------------------------------
    from pathlib import Path

    file_name = Path(__file__).stem + ".txt"
    input_file_path = Path().cwd() / r'large_inputs' / file_name
    print(f'Reading input from file at {input_file_path}.')
    with open(input_file_path, "r", encoding="utf8") as txt_file:
        T = int(txt_file.readline())
        for i in range(T):
            N, X = map(int, txt_file.readline().split())
            bottles_list = list(map(int,  txt_file.readline().split()))
            print(max_bottles_filled(sorted(bottles_list), X))
    # ----------------------------------------------------------

    """
    # HackerEarth Platform Input
    # ----------------------------------------------------------
    T = int(input())
    for i in range(T):
        N, X = map(int, input().split())
        bottles_list = list(map(int, input().split()))
        print(max_bottles_filled(sorted(bottles_list), X))
    """
