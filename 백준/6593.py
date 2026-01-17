import sys
import pprint
import heapq

diff = [
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (-1, 0, 0),
    (0, -1, 0),
    (0, 0, -1)
]



def dijkstra(start):
    heap = [start]
    heapq.heappush(heap, start)
    visited = [
                [
                    [False for _ in range(C)] for _ in range(R)
                ] for _ in range(L)
            ]

    while len(heap) != 0:
        m, l, r, c = heapq.heappop(heap)

        if visited[l][r][c] == True or buliding[l][r][c] == "#":
            continue

        visited[l][r][c] = True

        if buliding[l][r][c] == 'E':
            return m

        for ld, rd, cd in diff:
            if 0 <= l + ld < L and 0 <= r + rd < R and 0 <= c + cd < C:
                heapq.heappush(heap,(m + 1, l + ld, r+rd, c + cd))
            

    return -1





while True:
    L, R, C = map(int, sys.stdin.readline().split())
    if L == R == C == 0:
        exit(0)

    buliding = []
    for l in range(L):
        rows = []
        for r in range(R):
            row = sys.stdin.readline().strip()
            rows.append(row)
            if 'S' in row:
                start = (0, l, r, row.index("S"))

        buliding.append(rows)
        sys.stdin.readline()
    # pprint.pprint(buliding)

    m = dijkstra(start)
    if m != -1:
        print(f"Escaped in {m} minute(s).")
    else:
        print("Trapped!")


