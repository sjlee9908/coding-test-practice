import sys

SEC_MIN = 0
SEC_MAX = 1
SEC_STU = 2

def process(students):
    students.sort()
    sections = [[students[0][0], students[0][1], 0]]

    for a, b in students:
        for section in sections:
            if section[SEC_MIN] <= a <= section[SEC_MAX]:
                if section[SEC_MAX] <= b:
                    section[SEC_MAX] = b
                section[SEC_STU] += 1

            elif section[SEC_MIN] <= b <= section[SEC_MAX]:
                if section[SEC_MIN] >= a:
                    section[SEC_MIN] = a
                section[SEC_STU] += 1

            else:
                section.append([a, b])
        print(sections)

    res = 0
    for section in sections:
        res += min(section[SEC_STU], section[SEC_MAX] - section[SEC_MIN] + 1)
    return res


T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    students = []
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        students.append((a, b))
    print(process(students))
