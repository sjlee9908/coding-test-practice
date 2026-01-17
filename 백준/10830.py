#https://www.acmicpc.net/problem/10830
import sys


def mulMat(A, B):
    temp = [[0] * (len(B[0])) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(B[0])):
                temp[i][k] += A[i][j] * B[j][k]

    for i in range(N):
        for j in range(N):
            temp[i][j] %= 1000

    return temp

def powerMat(x, n) :
    for i in range(N):
        for j in range(N):
            x[i][j] %= 1000

    if n == 1 : # 종료조건
        return x
    elif (n % 2) == 0 : #n이 짝수
        return powerMat(mulMat(x,x), n // 2)
    else : # n이 홀수
        return mulMat(x, powerMat(mulMat(x,x), (n - 1) // 2))


N, b = map(int, sys.stdin.readline().split())
mat = []
for i in range(N):
    mat.append(list(map(int, sys.stdin.readline().split())))

res_mat = powerMat(mat, b)
for i in range(N):
    for j in range(N):
        print(res_mat[i][j],end = " ")
    print()
