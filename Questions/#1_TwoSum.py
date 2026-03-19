from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        curr = {}

        for i, v in enumerate(nums):

            if target - v not in curr:
                curr[v] = i

            else:
                return [i, curr[target-v]]
            
if __name__ == "__main__":
    print(Solution().twoSum([3,2,4], 6))
    print(Solution().twoSum([2,7,11,15], 9))
    print(Solution().twoSum([3,3], 6))
