import sys

N = int(sys.stdin.readline())
wrongs = list(map(int, sys.stdin.readline().split()))
rights = list(map(int, sys.stdin.readline().split()))

diffs = [wrongs[i] - rights[i] for i in range(N)]
res = 0


while True:
    diff_sections = []
    ex = diffs[0]
    li = []

    for diff in diffs:
        if ex * diff > 0:
            li.append(diff)

        else:
            if li != []: diff_sections.append(li)
            li = [diff]

        ex = diff

    if li != []: diff_sections.append(li)

    #print(diff_sections)
    #print(diffs)
    temp = 0
    i = 0
    for diff_section in diff_sections:
        if diff_section[0] > 0:
            mtemp = min(diff_section)
        else:
            mtemp = max(diff_section)

        for ii in range(len(diff_section)):
            diffs[i + ii] -= mtemp

        temp += abs(mtemp)
        i += len(diff_section)

    #print(diffs, temp)

    if temp == 0:
        break
    else:
        res += temp

print(res)