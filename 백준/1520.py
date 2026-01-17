# https://www.acmicpc.net/problem/1520
import collections
import sys

# input

graph = collections.deque()
row, col = map(int, sys.stdin.readline().split())
for i in range(row):
    graph.append(list(map(int, sys.stdin.readline().split())))

dp_table = [[0] * (col) for _ in range(row)]

# process
row_diff = [0, 1, 0, -1]
col_diff = [-1, 0, 1, 0]


def dfs(x, y, avail_count):

    ex_dp = dp_table[x][y]
    dp_table[x][y] += avail_count

    # print("now_x=", x, "now_y=", y, "avail_count=", avail_count)
    # for i in range(row):
    #     for j in range(col):
    #         print(dp_table[i][j], end=" ")
    #     print()
    # print()

    if x == row-1 and y == col -1:
        return


    for i in range(4):
        next_x, next_y = x + row_diff[i], y + col_diff[i]
        if 0 <= next_x < row and 0 <= next_y < col:
            if graph[next_x][next_y] < graph[x][y]:
                dfs(next_x, next_y, dp_table[x][y] - ex_dp)


dfs(0, 0, 1)

# for i in range(row):
#     for j in range(col):
#         print(dp_table[i][j], end=" ")
#     print()
# print()

print(dp_table[row - 1][col - 1])
