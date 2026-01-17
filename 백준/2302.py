import sys



pinned_seats = []
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
seat = [_ for _ in range(N)]
for _ in range(M):
    pinned_seats.append(int(sys.stdin.readline()) - 1)

dp_table = []
for i in range(len(seat)-1):
    if i + 1 or i in pinned_seats: continue
    dp_table.append(0)

dp_table.






