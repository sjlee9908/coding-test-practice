# import sys
#
# N = int(sys.stdin.readline())
# dp_table = [-1] * (101)
#
# dp_table[1] = 1
# dp_table[2] = 2
# dp_table[3] = 3
# dp_table[4] = 4
# dp_table[5] = 5
# dp_table[6] = 6
#
# for i in range(101):
#     for j in range(1, i-2):
#         dp_table[i] = max(
#             max(
#                 dp_table[i - 1] + 1,
#                 (dp_table[i - (j+2)] * (j + 1))
#             ), dp_table[i]
#         )
#
# print(dp_table[N])