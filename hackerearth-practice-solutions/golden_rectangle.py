# Golden rectangles

def is_golden_rectangle(length, breadth):
    if length > breadth:
        ratio = length / breadth
    else:
        ratio = breadth / length
    if 1.6 <= ratio <= 1.7:
        return True
    return False


if __name__ == "__main__":
    N = int(input())
    count = 0
    for i in range(1, N + 1):
        input_str = input().split()
        L = int(input_str[0])
        B = int(input_str[1])
        if is_golden_rectangle(L, B):
            count += 1
    print(count)
