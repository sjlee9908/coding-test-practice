# https://www.acmicpc.net/problem/1405
import collections
import sys

#input
n, east_prob, west_prob, south_prob, north_prob = map(int, sys.stdin.readline().split())

#process
prob = [east_prob/100, west_prob/100, south_prob/100, north_prob/100] #100프로가 기준인 확률을 1을 기준으로 다시 만들어줌
diff = [(1,0), (-1, 0), (0, -1), (0, 1)] #로봇의 동서남북 이동
sol = collections.defaultdict(lambda : False)  #방문기록 테이블
ans = 1.0  #로봇이 한 곳을 두번 방문하지 않을 확률 == 맨 처음은 1

def dfs(x, y, level, now_prob):
    global ans

    #가지치기 조건 == 1곳을 두번 방문
    if sol[(x, y)]:
        ans -= now_prob
        return

    #로봇 움직임 끝
    if level == n:
        return
    
    #방문기록
    sol[(x, y)] = True

    #dfs로 순회
    for i in range(4):
        x_diff, y_diff = diff[i]
        if prob[i] != 0.0:
            dfs(x+x_diff, y+y_diff, level + 1, now_prob * prob[i])

    sol[(x, y)] = False

dfs(0, 0, 0, 1)

#output
print(ans)