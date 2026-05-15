# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of conference rooms required.


# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2

# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: 1


# Constraints:
# 1 <= intervals.length <= 10**4
# 0 <= start[i] < end[i] <= 10**6


from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda i: i[0])

        res = [intervals[0]]
        output = 1

        for start, end in intervals[1:]:
            last_end = res[-1][1]
            if start < last_end:  ## cannot use the same room
                res.append([start, end])
                output += 1

            else:  ## [[1,5],[8,9],[8,9]]
                res[-1][1] = max(last_end, end)

            res.sort(key=lambda i: i[1], reverse=True)
            ## [[9,10],[4,9],[4,17]]
            ## [[4,9],[4,17],[9,10]]
            ## [[4,17],[4,9]]
            ## [[4,17],[4,10]]

        return output


if __name__ == "__main__":
    print(Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
    print(Solution().minMeetingRooms([[7, 10], [2, 4]]))
    print(Solution().minMeetingRooms([[1, 5], [8, 9], [8, 9]]))
    print(Solution().minMeetingRooms([[9, 10], [4, 9], [4, 17]]))
