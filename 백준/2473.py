# https://www.acmicpc.net/problem/2473
import sys

# input
n = int(sys.stdin.readline())
water = list(map(int, sys.stdin.readline().split()))

# processing
water.sort()
res = sys.maxsize
res_waters = [0, 0, 0]

#print(water)

for i in range(n - 2):
    left = i + 1
    right = n - 1
    ex_tmp = sys.maxsize
    while left < right:
        tmp = water[i] + water[left] + water[right]
        if abs(tmp) < abs(res):
            res = tmp
            res_waters = [water[i], water[left], water[right]]
        if tmp == 0:
            res_waters = [water[i], water[left], water[right]]
            res_waters.sort()
            print(res_waters[0], res_waters[1], res_waters[2])
            exit(0)
        elif tmp < 0:
            left += 1
        else:
            right -= 1
        ex_tmp = tmp

# output
res_waters.sort()
print(res_waters[0], res_waters[1], res_waters[2])
