# Meeting the origin

# My solution (All TCs passed)
def origin_after_operations(S):
    operations_count = 0
    dict_chars = Counter(S)
    sum_LR = dict_chars["L"] + dict_chars["R"]
    sum_UD = dict_chars["U"] + dict_chars["D"]
    min_LR = min(dict_chars["L"], dict_chars["R"])
    min_UD = min(dict_chars["U"], dict_chars["D"])

    if not sum_LR % 2 == 0:
        operations_count += 1
    operations_count += sum_LR//2 - min_LR

    if not sum_UD % 2 == 0:
        operations_count += 1
    operations_count += sum_UD//2 - min_UD

    print(operations_count)


if __name__ == "__main__":
    from collections import Counter
    T = int(input())
    for i in range(T):
        S = input()
        origin_after_operations(S)
