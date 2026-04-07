# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.


# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2

# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1

# Output: [1]

# Example 3:

# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

# Output: [1,2]



from collections import defaultdict
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        res = []
        d = defaultdict(list)
        for num in nums:
            if num not in d:
                d[num] = -1
            d[num] -= 1 

        for key, value in d.items():
            result.append([value, key])
        heapq.heapify(result)

        
        for i in range(k):
            min = heapq.heappop(result)
            
            res.append(min[1])
        return res
    


if __name__ == "__main__":
    print(Solution().topKFrequent([1,1,1,2,2,3], 2))
    print(Solution().topKFrequent([1], 1))
    print(Solution().topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))



        
        