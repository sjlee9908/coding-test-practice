import collections
import sys

#input
N, K = map(int, sys.stdin.readline().split())
graph = [[] * N for _ in range(N)]
ques = [collections.deque(), collections.deque()] #현 상황을 번갈아 저장할 que
init_que = []

for x in range(N):
    li = list(map(int, sys.stdin.readline().split()))
    for y in range(N):
        graph[x].append(li[y])
        #바이러스의 위치 저장
        if li[y] != 0:
            init_que.append((li[y], x, y))

#바이러스의 종류대로 정렬
init_que.sort()
ques[0] = collections.deque(init_que)
S, X, Y = map(lambda x: int(x)-1, sys.stdin.readline().split())
S += 1

diff_x = [-1, 0, 1, 0]
diff_y = [0, -1, 0, 1]

sec = 0

#BFS 수행
while sec < S and graph[X][Y] == 0:
    #que가 빌 때까지, que를 번갈아 가며 수행
    while len(ques[sec%2]) != 0:
        virus, x, y = ques[sec%2].popleft() #que에서 pop
        for to_x, to_y in zip(diff_x, diff_y):
            #증식
            if 0 <= x + to_x < N and 0 <= y + to_y < N:
                if graph[x+to_x][y+to_y] == 0:
                    graph[x+to_x][y+to_y] = virus
                    #증식한 바이러스 위치를 다음 큐에 넣음
                    ques[(sec+1)%2].append((virus, x+to_x, y+to_y))
    sec += 1 #초 증가


#출력
print(graph[X][Y])
