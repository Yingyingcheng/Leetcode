# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

from typing import Counter, List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        curr = {}

        for k, v in enumerate(nums):
            if v in curr:
                return True
            else:
                curr[v] = k

        return False


class Solution1:
    def containsDuplicate1(self, nums: List[int]) -> bool:

        d = Counter(nums)

        for k, v in d.items():
            if v > 1:
                return True
        
        return False



if __name__ == "__main__":
    print(Solution().containsDuplicate([1,2,3,1]))
    print(Solution().containsDuplicate([1,2,3,4]))
    print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
    print(Solution1().containsDuplicate1([1,2,3,1]))
    print(Solution1().containsDuplicate1([1,2,3,4]))
    print(Solution1().containsDuplicate1([1,1,1,3,3,4,3,2,4,2]))

