n = int(input())

for i in range(n):
    methods = input()
    input()
    arr = input()
    arr = arr[1:-1]
    arr = list(arr.split(","))

    pop_idx = 0
    count_R = 0
    flag = 0

    if "" in arr:
        arr.remove("")

    for method in methods:
        if method == "R":
            count_R += 1
            if pop_idx == 0:
                pop_idx = -1
            else:
                pop_idx = 0

        if method == "D":
            if len(arr) == 0:
                print("error")
                flag = 1
                break
            else:
                arr.pop(pop_idx)
    if flag ==0:
        if count_R % 2 == 0:
            print("["+",".join(arr)+"]")
        else:
            arr.reverse()
            print("["+",".join(arr)+"]")