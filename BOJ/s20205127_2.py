def rotateMat(mat):
    N = len(mat)-1
    if N%2 == 1:
        for i in range(0, len(mat)//2):
            for j in range(0, len(mat)):
                tmp = mat[i][j]
                mat[i][j] = mat[i+(N-2*i)][j+(N-2*j)]
                mat[i + (N - 2 * i)][j + (N - 2 * j)] = tmp
        return mat
    else:
        for i in range(0, len(mat)//2):
            for j in range(0, len(mat)):
                tmp = mat[i][j]
                mat[i][j] = mat[i+(N-2*i)][j+(N-2*j)]
                mat[i + (N - 2 * i)][j + (N - 2 * j)] = tmp
        tmp = mat[N//2][0]
        mat[N//2][0] = mat[N//2][N]
        mat[N // 2][N] = tmp
        return mat