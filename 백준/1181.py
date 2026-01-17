import collections

n = int(input())
word_list = set()

for i in range(n):
    s = input()
    word_list.add((len(s), s))

word_list = list(word_list)
word_list.sort(key = lambda x: (x[0], x[1]))

for i in word_list:
    print(i[1])
