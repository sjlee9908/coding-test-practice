import sys

#input
n = int(sys.stdin.readline())
water_list = list(map(int, sys.stdin.readline().split()))


#process
ans = []
min_sum = sys.maxsize

#정렬
water_list.sort()
#two-pointer 초기화
p1 = 0
p2 = n-1

#p1과 p2가 다를 때까지, 중앙으로 포인터 이동
while p1 != p2:
    #합계산
    new_sum = water_list[p1] + water_list[p2]
    new_sum_abs = abs(new_sum)

    #계산된 합이 기존 합보다 작으면 답 갱신
    if new_sum_abs < min_sum:
        min_sum = new_sum_abs
        ans = [water_list[p1], water_list[p2]]

    #합이 0이면 결과 출력
    if new_sum == 0:
        ans = [water_list[p1], water_list[p2]]
        break
    
    #합이 0보다 크면, 오른쪽 포인터를 중앙으로
    #왼쪽 포인터가 끝쪽으로 가지 않는 이유는, 정렬이 되어있어 외곽의 값들이 0에서 더 멀어지기 때문임
    elif new_sum > 0:
        p2 -= 1

    #합이 0보다 작으면, 왼쪽 포인터를 중앙으로
    elif new_sum < 0:
        p1 += 1

#output
print(ans[0], ans[1])




