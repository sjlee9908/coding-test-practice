class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distance = []
        res = []


        for i in points:
            distance.append(sum([x**2 for x in i]))

        distance = enumerate(distance)
        distance = sorted(distance, key=lambda x: x[1])

        print(distance)

        for i in range(k):
            res.append(points[distance[i][0]])

        return res
sol = Solution()
print(sol.kClosest([[1,3], [-2,2]], 1))


