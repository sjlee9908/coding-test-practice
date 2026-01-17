# https://www.acmicpc.net/problem/17297
import sys

#input
m = int(sys.stdin.readline())

#process
# N번째 수열의 길이를 저장하는 dp table
dp_table = {1: 5, 2 : 13}

#dp테이블에 저장된 길이를 통해 다음 길이를 채워넣음과 동시에, 현재 m이 몇번 수열에 속하는 지 알아내는 함수
def get_n():
    i = 2
    while dp_table[i] < m:  
        i += 1
        dp_table[i] = dp_table[i-1] + 1 + dp_table[i-2]
    return i

#n이 2이하인 경우의 코너 케이스 핸들링
if m <= 13:
    if "Messi Gimossi"[m-1] == " ":
        print("Messi Messi Gimossi")
    else:
        print("Messi Gimossi"[m-1])
    exit(0)

#M번째 글자가 몇 번째 수열 다음에 속하는 지 확인한다.
i = get_n() - 1
#m이 13이하가 될 때 까지
while m > 13:
    #계산된 바에 따라 다시 m을 재계산한다.
    new_m = m - dp_table[i] - 1
    #m은 0 이상이어야 한다.
    if new_m >= 0: m = new_m
    #다음 m을 계산하기 위해 이전 수열의 길이를 고려한다.
    i -= 1

if m <= 13:
    #0혹은 6번째는 공백임
    if m == 0 or m == 6:
        print("Messi Messi Gimossi")
    #그외는 글자 출력
    else:
        print("Messi Gimossi"[m-1])
    exit(0)