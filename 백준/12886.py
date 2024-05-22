import collections
import sys

a, b, c = map(int, sys.stdin.readline().split())
visit_table = collections.defaultdict(lambda : False)

stone_select = [(0, 1, 2), (1, 2, 0), (0, 2, 1)]

def bfs(a, b, c):
    que = collections.deque()
    que.append(sorted((a, b, c)))

    while len(que) != 0:
        stones = que.popleft()
        #print(stones)
        visit_table[tuple(stones)] = True

        if stones[0] == stones[1] == stones[2]:
            return 1

        for select in stone_select:
            if stones[select[0]] != stones[select[1]]:
                x = min(stones[select[0]], stones[select[1]])
                y = max(stones[select[0]], stones[select[1]])

                new_stone = sorted((x + x, y - x, stones[select[2]]))

                if new_stone[0] == new_stone[1] == new_stone[2]:
                    return 1

                if visit_table[tuple(new_stone)] != True:
                    que.append(new_stone)

    return 0

print(bfs(a, b, c))



