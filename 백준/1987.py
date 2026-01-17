import collections
import sys

sys.setrecursionlimit(10 ** 4)

# input
r, c = map(int, sys.stdin.readline().split())
board = [list(map(lambda x: ord(x) - 65, sys.stdin.readline())) for i in range(r)]

# process
max_distance = 1
path_book = [False] * 26
next_move_r = [-1, 1, 0, 0]
next_move_c = [0, 0, 1, -1]


def dfs(r_idx, c_idx, distance):
    global path_book
    global max_distance

    now_char = board[r_idx][c_idx]
    if board[r_idx][c_idx] == "" or path_book[now_char]:
        return

    max_distance = max(max_distance, distance)
    path_book[now_char] = True

    for i in range(4):
        next_r_idx = r_idx + next_move_r[i]
        next_c_idx = c_idx + next_move_c[i]
        if 0 <= next_r_idx < r and 0 <= next_c_idx < c and path_book[board[next_r_idx][next_c_idx]] == False:  #이 부분 추가
            dfs(next_r_idx, next_c_idx, distance + 1)

    path_book[now_char] = False


dfs(0, 0, 1)

# output
print(max_distance)
