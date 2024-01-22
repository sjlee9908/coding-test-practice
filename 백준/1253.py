import collections
import sys

n = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

if len(nums) < 3:
    print(0)
    exit(0)

nums.sort(reverse=True)
nums_dict = collections.defaultdict(int)
good_count = 0

for num in nums:
    nums_dict[num] += 1

for idx, target in enumerate(nums):
    nums_dict[target] -= 1
    for num1 in nums[:idx] + nums[idx + 1:]:
        nums_dict[num1] -= 1

        if nums_dict[target - num1] > 0:
            #print(target, num1, target - num1)
            good_count += 1
            nums_dict[num1] += 1
            break

        nums_dict[num1] += 1
    nums_dict[target] += 1

print(good_count)
