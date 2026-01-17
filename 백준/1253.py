import collections
import sys

#input
n = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

#process
#corner case 처리
if len(nums) < 3:
    print(0)
    exit(0)

#정렬
nums.sort(reverse=True)
nums_dict = collections.defaultdict(int)
good_count = 0

#수 인덱싱
for num in nums:
    nums_dict[num] += 1

for idx, target in enumerate(nums):
    #target이 좋은 수인지 판별
    nums_dict[target] -= 1
    
    #target을 제외한 N-1개 수를 검사
    for num1 in nums[:idx] + nums[idx + 1:]:
        #num1을 통해 target이 구성되는지 검사
        nums_dict[num1] -= 1

        #target-num1이 존재하는지 검사
        if nums_dict[target - num1] > 0:
            #존재하면 good_count + 1, target에 대한 좋은 수 검사 중지
            good_count += 1
            nums_dict[num1] += 1   # 사용한 수 원상 복구
            break

        #사용한 수 원상 복구
        nums_dict[num1] += 1
    nums_dict[target] += 1

#output
print(good_count)
