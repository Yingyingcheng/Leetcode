# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers sum to target. 
# You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# Example 3:

# Input: candidates = [2], target = 1
# Output: []
 

# Constraints:

# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40

from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i, curSum, curcomb):

            if curSum == target:
                res.append(curcomb.copy())
                return

            if i >= len(candidates) or curSum > target:
                return


            # Decision 1: Include candidates[i] (can stay on same index to reuse it)
            curcomb.append(candidates[i])
            dfs(i, curSum + candidates[i], curcomb)

            # Decision 2: Backtrack and skip candidates[i]  
            curcomb.pop()
            dfs(i+1, curSum, curcomb)

        dfs(0, 0, [])
        return res 



if __name__ == "__main__":
    print(Solution().combinationSum([2,3,6,7], 7))
    print(Solution().combinationSum([2,3,5], 8))
    print(Solution().combinationSum([2], 1))




#                     dfs(0, [], total=0)
#                    /                   \
#         Include 2 /                     \ Skip 2
#                  v                       v
#       dfs(0, [2], total=2)         dfs(1, [], total=0)
#             /          \
#   Include 2/            \ Skip 2
#           v              v
# dfs(0, [2,2], total=4)  dfs(1, [2], total=2)