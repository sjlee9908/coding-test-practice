list_nums = list(map(int, list(input())))
list_nums.sort(reverse=True)

if list_nums[-1] != 0:
    print(-1)
    exit(0)

if sum(list_nums) % 3 != 0:
    print(-1)
    exit(0)

list_nums = list(map(str, list_nums))
s = str()
s = "".join(list_nums)
print(s)