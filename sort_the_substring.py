# Sort the Substring

def sorted_string(S_str, N_pos, M_pos):
    str_part_1 = S_str[:N_pos]
    str_part_2 = S_str[M_pos+1:]
    substring_str = ''.join(sorted(S_str[N_pos: M_pos+1], reverse = True))
    return str_part_1 + substring_str + str_part_2



if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        S_str, N_pos, M_pos = input().split()
        print(sorted_string(S_str, int(N_pos), int(M_pos)))