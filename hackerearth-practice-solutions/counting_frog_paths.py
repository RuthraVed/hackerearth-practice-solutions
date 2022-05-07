# Counting Frog Paths

def counting_frog_paths(x_axis, y_axis, s_side, t_secs):
    count = 0
    for i in range(0, s_side + 1):
        # This outer loop increments x
        for j in range(0, s_side + 1):
            # This inner loop increments y
            if ((x_axis + i) + (y_axis + j)) <= t_secs:
                count += 1
    return count


if __name__ == "__main__":
    X_axis, Y_axis, s_side, T_secs = map(int, input().split())
    print(counting_frog_paths(X_axis, Y_axis, s_side, T_secs))
