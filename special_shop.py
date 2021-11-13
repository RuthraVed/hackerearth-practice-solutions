# Special Shop
from math import pow


def minimum_purchase_cost(n_pots, a_cost, b_cost):
    min_cost = 0
    for i in range(0, n_pots):
        total_cost = a_cost * pow(i, 2) + b_cost * pow(n_pots - i, 2)

        # Storing any initial purchase cost
        if i == 0:
            min_cost = total_cost

        # Check to store min. cost
        if min_cost > total_cost:
            min_cost = total_cost

    return min_cost


if __name__ == "__main__":
    T = int(input())
    for i in range(0, T):
        N_pots, A_cost, B_cost = map(int, input().split())
        print(minimum_purchase_cost(N_pots, A_cost, B_cost))
