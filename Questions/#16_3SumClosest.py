# Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        closetSum = float("inf")

        for i, a in enumerate(nums):

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:

                curSum = a + nums[l] + nums[r]

                if curSum == target:
                    return curSum

                if abs(curSum - target) < abs(closetSum - target):
                    closetSum = curSum

                if curSum < target:
                    l += 1
                elif curSum > target:
                    r -= 1

        return closetSum


if __name__ == "__main__":
    print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
    print(Solution().threeSumClosest([0, 0, 0], 1))
    print(Solution().threeSumClosest([10, 20, 30, 40, 50, 60, 70, 80, 90], 60))
