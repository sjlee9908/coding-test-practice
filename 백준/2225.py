import sys

#input
n, k = map(int, sys.stdin.readline().split())

#process
#dp_table 선언
dp_table = [[-1] * (k+1) for _ in range(n+1)]

def dfs(now_n, now_k):
    #dp_table 확인
    if dp_table[now_n][now_k] != -1:
        return dp_table[now_n][now_k]

    #바닥상태, 만약 k가 1이하면, 가능한 경우의 수는 단 1개임
    if now_k <= 1:
        return 1


    tmp = 0
    #n이 아닌 now_n까지만 반복문을 돌리는 이유: n-i에서 n까지 반복문을 돌리면 음수를 고려해야함
    for i in range(now_n+1):
        #now_n 축소, now_k 축소
        tmp += dfs(now_n - i, now_k-1)
    #dp_table 채우기
    dp_table[now_n][now_k] = tmp

    return dp_table[now_n][now_k]

#output
print(dfs(n, k)%1000000000)