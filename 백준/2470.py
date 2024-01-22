import sys

n = int(sys.stdin.readline())
water_list = list(map(int, sys.stdin.readline().split()))
ans = [sys.maxsize, s]
min_sum = sys.maxsize

water_list.sort()
p1 = n//2
p2 = n//2+1

while p1 >= 0 and p2 <= len(water_list)-1:
    new_sum = water_list[p1] + water_list[p2]
    new_sum_abs = abs(new_sum)

    if new_sum_abs < min_sum:
        min_sum = new_sum_abs
        ans = [water_list[p1] + water_list[p2]]

    if new_sum == 0:
        ans = [water_list[p1] + water_list[p2]]
        break

    elif new_sum > 0:
        p1 -= 1

    elif new_sum < 0:
        p2 += 1

print(ans[0], ans[1])




