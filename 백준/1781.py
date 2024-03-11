# https://www.acmicpc.net/problem/1781
import heapq
import sys

#input
n = int(sys.stdin.readline())
plist = []
for _ in range(n):
    #deadline = 이 숙제를 내기 전 deadline개의 숙제를 할 수 있다는 뜻
    deadline, cup = map(int, sys.stdin.readline().split())
    plist.append((deadline, cup))

#process
plist.sort()  #문제들을 오름차순 정렬 -> 데드라인, 컵라면수 순서로
do_plist = [] #"풀" 문제들의 컵라면 수를 저장하는 heap

#전체 문제를 고려
for deadline, cup in plist:
    #문제 고려, 이때 고려되는 문제는 같은 deadline이라면 heap에 들어간 컵라면수보다 높음
    heapq.heappush(do_plist, cup)

    #고려를 해봤는데, 이 문제를 풀기엔 deadline이 맞지 않음 -> heap에서 뺌 -> 이 코드블록 때문에, do_plist는 최대 deadline개수임이 보장됨
    #고려를 해봤는데, 이 문제를 풀기엔 deadline이 맞음 -> heap에서 빼지 않음
    if len(do_plist) > deadline:
        #빼는 문제는 가장 작은 컵라면을 주는 문제
        heapq.heappop(do_plist)

#output
print(sum(do_plist))