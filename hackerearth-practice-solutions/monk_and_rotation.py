# Monk and Rotation

def rotate_array(N, K , input_arr):
    new_arr = [0] * N
    for i in range(N):
        new_pos = (i+K)%N   # Using modulus as we need a circular rotation
        new_arr[new_pos] = input_arr[i]
    return new_arr

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N, K = map(int, input().split())
        input_arr = input().split()
        rotated_arr = rotate_array(N, K , input_arr)
        print(" ".join(rotated_arr))