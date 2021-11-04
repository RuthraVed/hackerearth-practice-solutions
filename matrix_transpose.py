# Matrix Transpose
''' Program to transpose a matrix using list comprehension'''

def transpose_matrix(M, N, original_matrix):
    rows, cols = N, M
    matrix_T = [[0 for j in range(cols)] for i in range(rows)]
    for j in range(cols):
        for i in range(rows):
            matrix_T[i][j] = original_matrix[j][i]
    return matrix_T



if __name__ == "__main__":
    M, N = map(int, input().split())    
    input_matrix = [0] * M
    for i in range(M):
        input_matrix[i] = input().split()
    output_matrix = transpose_matrix(M, N, input_matrix)
    for i in range(N):
        print(' '.join(output_matrix[i]))