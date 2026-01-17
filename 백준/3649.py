import sys

while True:
    #input
    X = sys.stdin.readline()
    if X == "": break  #입력이 EOF인 경우 종료
    X = int(X) * 10000000
    N = int(sys.stdin.readline())
    
    lengths = []
    for _ in range(N):
        lengths.append(int(sys.stdin.readline()))

    #process
    #정렬
    lengths.sort()
    
    #two-pointer 선언
    i = 0
    j = len(lengths) - 1

    #가운데로 이동
    while i < j:
        s = lengths[i] + lengths[j]
        #hit
        if s == X:
            print("yes", lengths[i], lengths[j])
            break
        #합을 작게
        elif s > X:
            j -= 1
        #합을 크게
        else:
            i += 1
    
    #합이 X가 되는 경우가 없을 경우
    if i >= j:
        print("danger")



