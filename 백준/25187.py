import sys

N, M, Q = map(int, sys.stdin.readline().split())
N = N-1
water = list(map(int, sys.stdin.readline().split()))
graph = []
disjoint_set = []
