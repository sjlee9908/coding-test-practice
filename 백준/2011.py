import collections
import sys

#재귀한도 설정
sys.setrecursionlimit(10 ** 4)

#input
num_string = sys.stdin.readline().rstrip()
dp_table = collections.defaultdict(lambda : -1)

#process
#dp_table 초기값 설정
#1개 해석이 가능한 경우
for i in range(1, 11):
    dp_table[str(i)] = 1
#2개 해석이 가능한 경우
for i in range(11, 27):
    dp_table[str(i)] = 2
#20은 예외로 1개 해석이 가능함
dp_table["20"] = 1

#get_encrypt()함수
def dfs(num_s):
    #''이나 '0'인 경우는 해석이 불가능
    if num_s == '' or num_s[0] == '0':
        return 0

    #dp 적용
    if dp_table[num_s] != -1:
        return dp_table[num_s]

    # 해석 개수 계산
    tmp = 0
    # 2개 해석이 가능한 경우는 첫 2자리 숫자가 26이하인 경우임
    if int(num_s[0:2]) <= 26:
        tmp += dfs(num_s[2::])
    # 1개 해석이 가능한 경우는 첫 2자리 숫자가 26이상인 경우임
    # 이러나 저러나 첫 문자를 제외한 해석은 항상 가능함
    tmp += dfs(num_s[1::])

    #저장 후 return
    dp_table[num_s] = tmp % 1000000
    return dp_table[num_s]

#output
print(dfs(num_string))
