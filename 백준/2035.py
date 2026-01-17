# https://www.acmicpc.net/problem/2035
import sys

# input
s = sys.stdin.readline().rstrip()

# process
ans = int(s)


def dfs(before_s, now_s):
    global ans

    # 정답 갱신
    ans = min(ans, int(now_s))

    # dfs 수행, (n/2-1)자리의 숫자는 (n/2+1)보다 클 수 없음 -> 고려할 가짓수가 절반 감소
    for i in range(len(now_s) // 2 + 1):
        # 문자열 추출
        next_s = now_s[i + 1:]
        calc_s = now_s[0:i + 1]

        # end조건
        if next_s == "" or calc_s == "" or before_s == "":
            return

        # 가지치기 수행
        if int(before_s) < int(calc_s) < int(next_s):
            dfs(calc_s, next_s)


dfs("0", s)

# output
print(ans)



