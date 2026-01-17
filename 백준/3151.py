# https://www.acmicpc.net/problem/3151
import sys

# input
n = int(sys.stdin.readline())
students = list(map(int, sys.stdin.readline().split()))

# process
students.sort()
res = 0
#print(students)
for i in range(n - 2):
    s1 = students[i]
    left, right = i + 1, n - 1

    while left < right:
        s2, s3 = students[left], students[right]
        team = s1 + s2 + s3

        if team == 0:
            if s2 == s3:
                tmp = right - left+1
                res += (tmp * (tmp-1)) // 2
                break
            else:
                r_same = 1
                while s3 == students[right - 1]:
                    right -= 1
                    r_same += 1
                l_same = 1
                while s2 == students[left + 1]:
                    left += 1
                    l_same += 1
                res += (r_same * l_same)
            left += 1
            right -= 1

        elif team < 0:
            left += 1

        else:
            right -= 1
# output
print(res)
