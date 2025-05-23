import sys

N = 9
sudoku = []
blanks = []
for i in range(N):
    s = sys.stdin.readline().rstrip()
    li = []
    for idx, n in enumerate(s):
        if n =="0":
            blanks.append((i, idx))
        li.append(int(n))
    sudoku.append(li)



def dfs(n):
    if n == len(blanks):
        for li in sudoku:
            for i, num in enumerate(li):
                if i != 8: print(num, end = "")
                else: print(num, end = "")
            print()
        exit(0)

    fill_row, fill_col = blanks[n]
    nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    #가로 줄 체크
    for i in range(N):
        nums[sudoku[fill_row][i]] = 1

    #세로 줄 체크
    for i in range(N):
        nums[sudoku[i][fill_col]] = 1

    #3x3칸 체크
    start_row = (fill_row // 3) * 3
    end_row = (fill_row // 3) * 3 + 3
    start_col = (fill_col // 3) * 3
    end_col = (fill_col // 3) * 3 + 3
    for i in range(start_row, end_row):
        for j in range(start_col, end_col):
            nums[sudoku[i][j]] = 1


    #채우기 -> 가능한 것으로만 = 하나도 없으면 return
    for i in range(1, len(nums)):
        if nums[i] == 0:
            sudoku[fill_row][fill_col] = i
            dfs(n+1)
            sudoku[fill_row][fill_col] = 0
    return


dfs(0)