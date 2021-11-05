# Minimum AND xor OR

def min_AND_xor_OR(N, arr):
    arr.sort()
    min = arr[0] ^ arr[1]   # Consider min, at 0th position
    for i in range(1, N-1):
        temp = arr[i] ^ arr[i+1]
        if temp < min:
            min = temp
    return min


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        print(min_AND_xor_OR(N, arr))
        


if __name__ == "__main__":
    # T = int(input())
    # for i in range(T):
    #     N = int(input())
    #     arr = list(map(int, input.split()))
    #     print(min_AND_xor_OR(N, arr))

    N = 3
    arr = [2, 4, 7]
    print(min_AND_xor_OR(N, arr))
        