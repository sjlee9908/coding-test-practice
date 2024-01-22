# https://www.acmicpc.net/problem/14621
import collections
import sys

N, M = map(int, sys.stdin.readline().split())
N_gender = list(sys.stdin.readline().split())

graph = [collections.deque() for _ in range(N)]
e_list = collections.deque()

for i in range(M):
    u, v, d = map(lambda x: int(x)-1, sys.stdin.readline().split())
    graph[u].append((u, v, d+1))
    graph[v].append((v, u, d+1))
    e_list.append((u, v, d+1))

class DisJointSet:
    def __init__(self, n):
        self.set_ = [-1] * n
        self.set_count_ = n

    def find(self, n):
        while self.set_[n] != -1:
            n = self.set_[n]
        return n
    def union(self, n1, n2):
        self.set_[n1] = n2
        self.set_count_ -= 1


def MST():
    global e_list
    e_list = sorted(e_list, key = lambda e: e[2])
    dset = DisJointSet(N)

    total_d = 0
    e_count = 0
    #print(e_list)
    for i in range(M):
        u, v, d = e_list[i]
        us = dset.find(u)
        vs = dset.find(v)

        if us != vs and N_gender[u] != N_gender[v]:
            dset.union(us, vs)
            #print((u, v, d), N_gender[u], N_gender[v])
            total_d += d
            e_count += 1
            if e_count == N-1:
                return total_d
    return -1

print(MST())

