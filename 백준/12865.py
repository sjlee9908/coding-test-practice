import sys

#input
n, k = map(int, sys.stdin.readline().split())
items = []
for i in range(n):
    items.append(tuple(map(int, input().split())))

#process
#dp_table 구성 : 연산결과 저장
dp_table = [[-1] * (k + 1) for _ in range(n + 1)]

#knapsack(n, k)
def dfs(now_n, now_w):
    #dp = 연산한거 또 안 하기
    if dp_table[now_n][now_w] != -1:
        return dp_table[now_n][now_w]

    #문제의 바닥조건 = 재귀의 종료조건
    if now_n == 0 or now_w == 0:
        return 0

    #물건을 가방에 넣은 경우
    within = -1
    if now_w >= items[now_n-1][0]:
        within = dfs(now_n-1, now_w-items[now_n-1][0]) + items[now_n-1][1]

    #물건을 가방에 넣지 않은 경우 계산 후 dp_table 채우기
    dp_table[now_n][now_w] = max(within, dfs(now_n-1, now_w))

    #return
    return dp_table[now_n][now_w]

#output
print(dfs(n, k))


