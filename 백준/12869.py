import sys

N = int(sys.stdin.readline())
scvs = list(map(int, sys.stdin.readline().split()))
while len(scvs) <= 3: scvs.append(0)
dp_table = [[[None] * 61 for _ in range(61)] for _ in range(61)]
atk_way = [
    [9,3,1],
    [9,1,3],
    [3,9,1],
    [3,1,9],
    [1,3,9],
    [1,9,3]
]

dp_table[0][0][0] = 0

def dfs(now_scvs):
    for idx, scv in enumerate(now_scvs):
        if scv < 0: now_scvs[idx] = 0

    if dp_table[now_scvs[0]][now_scvs[1]][now_scvs[2]] != None:
        return dp_table[now_scvs[0]][now_scvs[1]][now_scvs[2]]

    tmp = sys.maxsize
    for atk in atk_way:
        tmp = min(tmp,
                    dfs([now_scvs[0]-atk[0], now_scvs[1]-atk[1], now_scvs[2]-atk[2]])
                  )
    dp_table[now_scvs[0]][now_scvs[1]][now_scvs[2]] = tmp + 1
    return tmp + 1

print(dfs(scvs))