# Monk and Inversions

def monks_inversion(M, N, input_matrix):
    counter = 0
    for i in range(M):
        for j in range(N):
            for l in range(i,M):
                for m in range(j,N):
                    if input_matrix[i][j] > input_matrix[l][m]:
                        counter = counter + 1
    return counter
    
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        M = N
        input_matrix = []
        for i in range(N):
            input_matrix.append(list(map(int, input().split())))
        print(monks_inversion(M, N, input_matrix))