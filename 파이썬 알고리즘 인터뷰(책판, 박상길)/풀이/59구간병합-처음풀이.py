class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = set([tuple(x) for x in intervals])
        intervals = list([list(x) for x in intervals])
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        i = 0

        while len(intervals) != 1 and i != len(intervals):
            if i != len(intervals)-1:
                if intervals[i][1] in range(intervals[i+1][0], intervals[i+1][1]+1):
                    intervals[i+1][0] = intervals[i][0]
                    intervals.pop(i)
                if not (len(intervals) != 1 and i != len(intervals)):
                    break
            if i != 0:
                if intervals[i][0] in range(intervals[i - 1][0], intervals[i - 1][1] + 1) and intervals[i][0] in range(
                        intervals[i - 1][0], intervals[i - 1][1] + 1):
                    intervals[i-1][1] = max(intervals[i][1], intervals[i-1][1])
                    intervals.pop(i)
                else:
                    i = i + 1
                    continue
                if not (len(intervals) != 1 and i != len(intervals)):
                    break
            if i == 0:
                i = i+1

        return intervals