import sys

#input
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

#process
dp_table = [[None] * 21 for _ in range(N)]  #결과의 가짓수를 저장(ex: dp_table[n][m]은 n번째 수까지 계산했을때, m을 만들 수있는 가짓수) 

def dfs(n, now_res):
    #종료: 음수, 20이상일때는 계산 불가
    if not (0 <= now_res <= 20):
        return 0

    #종료: 1번째 수까지 고려가 끝났을 때
    if n == 1:
        #0번째 수를 고려: 현재의 수가 0번째 수와 같음 -> 가능
        #0번째 수는 항상 더해짐
        if now_res == nums[0]:
            dp_table[n][now_res] = 1
            return dp_table[n][now_res]
        #0번째 수를 고려: 현재의 수가 0번째 수와 같지 않음 -> 불가능
        else: return 0

    #DP
    if dp_table[n][now_res] is not None:
        return dp_table[n][now_res]

    #dp_table 채우기
    dp_table[n][now_res] = dfs(n - 1, now_res + nums[n - 1]) + dfs(n - 1, now_res - nums[n - 1])

    return dp_table[n][now_res]

#output
#N-1까지 고려했을 때, nums[-1]이 나와야 함
print(dfs(N-1, nums[-1]))
# print(*dp_table, sep="\n")