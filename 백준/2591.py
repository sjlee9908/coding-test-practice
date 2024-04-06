import collections
import sys

nums = sys.stdin.readline().rstrip()
dp_table = collections.defaultdict(lambda : -1)
for i in range(1, 11):
    dp_table[str(i)] = 1
for i in range(11, 35):
    dp_table[str(i)] = 2
dp_table["20"] = 1
dp_table["30"] = 1


def dfs(nums):
    if dp_table[nums] != -1:
        return dp_table[nums]

    if nums == '' or nums[0] == '0':
        return 0
    else:
        if int(nums[0:2]) >= 34 or int(nums[0:2]) == 20 or int(nums[0:2]) == 10:
            dp_table[nums] = dfs(nums[1:])
        else:
            dp_table[nums] = dfs(nums[2:]) + dfs(nums[1:])
        return dp_table[nums]

print(dfs(nums))