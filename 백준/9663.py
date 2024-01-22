import sys

n = int(sys.stdin.readline())

row_lookup_table = [-1] * (n+1)
col_lookup_table = [False] * (n+1)
case_count = 0

def isSafe(y):
    for y_ in range(y):
        if row_lookup_table[y_] == row_lookup_table[y] or abs(row_lookup_table[y] - row_lookup_table[y_]) == y-y_:
            return False
    return True

def dfs(y):
    global case_count

    if y == n:
        case_count += 1
        return

    for x in range(n):
        if col_lookup_table[x]:
            continue
        row_lookup_table[y] = x
        if isSafe(y):
            col_lookup_table[x] = True
            dfs(y+1)
            col_lookup_table[x] = False
dfs(0)
print(case_count)
