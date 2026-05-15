# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.


# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false

# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: true


# Constraints:

# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti < endi <= 106


from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        intervals.sort(key=lambda i: i[0])

        if not intervals:
            return True

        res = [intervals[0]]

        for start, end in intervals[1:]:

            last_end = res[-1][1]

            if start < last_end:
                return False

            else:
                res.append([start, end])

        return True


if __name__ == "__main__":
    print(Solution().canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
    print(Solution().canAttendMeetings([[7, 10], [2, 4]]))
