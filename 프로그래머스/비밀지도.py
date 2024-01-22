#https://school.programmers.co.kr/learn/courses/30/lessons/17681
def solution(n, arr1, arr2):
    answer = []
    num = 2 ** n - 1

    for i in range(n):
        tmp = bin(arr1[i] | arr2[i] & num)[2:]
        s = ""
        while len(tmp) != n:
            tmp = "0" + tmp
        for c in tmp:
            if c == "0":
                s = s + " "
            else:
                s = s + "#"
        answer.append(s)



    return answer

print(solution(	6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))