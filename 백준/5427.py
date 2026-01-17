import collections
import sys

def bfs():
    fire_expansion()
    player_que = collections.deque([player, (sys.maxsize,sys.maxsize)])
    sec = 1

    while len(player_que) != 1:
        y, x = player_que.popleft()

        if y == 0 or y == H - 1 or x == 0 or x == W - 1:
            return sec

        if y == sys.maxsize and x == sys.maxsize:
            fire_expansion()
            sec += 1
            player_que.append((sys.maxsize, sys.maxsize))
            continue


        for dy, dx in diff:
            if 0 <= dy + y < H and 0 <= dx + x < W and building[dy + y][dx + x] == ".":
                player_que.append((dy + y, dx + x))
                row = building[dy + y]
                row = row[:dx + x] + "@" + row[dx + x + 1:]
                building[dy + y] = row

    return "IMPOSSIBLE"


def fire_expansion():
    global fires

    while True:
        y, x = fires.popleft()

        if y == sys.maxsize and x == sys.maxsize:
            fires.append((sys.maxsize, sys.maxsize))
            return

        for dy, dx in diff:
            if 0 <= dy + y < H and 0 <= dx + x < W and building[dy + y][dx + x] == "." :
                fires.append((dy + y, dx + x))
                row = building[dy + y]
                row = row[:dx + x] + "*" + row[dx + x + 1:]
                building[dy + y] = row



T = int(sys.stdin.readline())

diff = [
    (0, 1), (1, 0), (0, -1), (-1, 0)
]

for _ in range(T):
    W, H = map(int, sys.stdin.readline().split())
    fires = collections.deque()
    building = []
    player = (0, 0)

    for h in range(H):
        li = sys.stdin.readline().rstrip()
        for w, char in enumerate(li):
            if char == "*": fires.append((h, w))
            elif char == "@": player = (h, w)

        building.append(li)
    fires.append((sys.maxsize, sys.maxsize))
    print(bfs())




