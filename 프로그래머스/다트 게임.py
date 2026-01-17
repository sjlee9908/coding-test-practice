#https://school.programmers.co.kr/learn/courses/30/lessons/17682
def solution(dartResult):
    p = [0, 0, 0]
    dartResult_i = 0
    try_count = -1

    while dartResult_i < len(dartResult):
        if dartResult[dartResult_i].isdigit():
            try_count += 1
            if dartResult[dartResult_i + 1].isdigit():
                p[try_count] = int(dartResult[dartResult_i] + dartResult[dartResult_i + 1])
                dartResult_i += 1
            else:
                p[try_count] = int(dartResult[dartResult_i])

        elif dartResult[dartResult_i] == "S":
            pass
        elif dartResult[dartResult_i] == "D":
            p[try_count] **= 2
        elif dartResult[dartResult_i] == "T":
            p[try_count] **= 3
        elif dartResult[dartResult_i] == "*":
            p[try_count] *= 2
            p[try_count-1] *= 2
        elif dartResult[dartResult_i] == "#":
            p[try_count] *= -1

        dartResult_i += 1

    return sum(p)

print(solution("1D2S#10S"))