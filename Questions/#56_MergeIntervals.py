# Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Example 3:
# Input: intervals = [[4,7],[1,4]]
# Output: [[1,7]]
# Explanation: Intervals [1,4] and [4,7] are considered overlapping.

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda i: i[0])

        res = [intervals[0]]

        for start, end in intervals[1:]:

            last_end = res[-1][1]

            if start <= last_end:
                res[-1][1] = max(last_end, end)
                ## edge case: [[1, 10], [2, 6], [8, 10]]
                ## edge case: [[1, 7], [2, 6]]

            else:
                res.append([start, end])

        return res


if __name__ == "__main__":
    print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(Solution().merge([[1, 4], [4, 5]]))
    print(Solution().merge([[4, 7], [1, 4]]))
    print(Solution().merge([[1, 10], [2, 6], [8, 10]]))


## 1.   Time Complexity: O(N log N)
## (1). Sorting : In Python, Timsort has a complexity of O(N log N).
## (2). Linear Scan : After sorting, the script iterates through the list exactly once using a for loop:
##      for start, end in intervals[1:]. Inside this loop, all operations (comparing values and appending to a list) are O(1).
## (3). Total: O(N log N) + O(N) simplifies to O(N log N).


## 2.   Space Complexity: O(N)
## (1). Result List (O(N)): You create a new list res to store the merged intervals. In the worst case (where no intervals overlap), res will contain N intervals, requiring O(N) space.
## (2). Sorting Space (O(N)): Python’s sort() method (Timsort) typically requires up to O(N) additional space for temporary storage during the sorting process.
## (3). Total: The overall auxiliary space complexity is O(N).


## Follow up: Can you do this in-place to save space?

## While you could modify the input list directly to achieve O(1) extra space (excluding the space for sorting),
## it is usually safer to return a new list. This prevents side effects, meaning the original data remains unchanged for other parts of the application—a "Senior" practice that is highly valued in React/TypeScript development where immutability is key.
