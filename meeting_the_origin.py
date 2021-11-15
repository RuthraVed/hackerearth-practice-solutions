# Meeting the origin

# Problem setter's solution
def origin_after_operations(s):
    print((abs(s.count('L') - s.count('R')) + 1) // 2 + (abs(s.count('U') - s.count('D')) + 1) // 2)


if __name__ == "__main__":
    from collections import Counter
    T = int(input())
    for i in range(T):
        S = input()
        origin_after_operations(S)
