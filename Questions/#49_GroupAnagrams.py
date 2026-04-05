# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.


from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:

        d = defaultdict(list)
        
        for w in strs:

            count = [0] * 26
            for c in w:
                count[ord(c) - ord('a')] += 1

            
            d[tuple(count)].append(w)

        return list(d.values())
    
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        for w in strs:

            sorted_str = ''.join(sorted(w))
            d[sorted_str].append(w)
        return list(d.values())

if __name__ == "__main__":
    print(Solution().groupAnagrams1(["eat","tea","tan","ate","nat","bat"]))
    print(Solution().groupAnagrams1([""]))
    print(Solution().groupAnagrams1(["a"]))
    print(Solution().groupAnagrams2(["eat","tea","tan","ate","nat","bat"]))
    print(Solution().groupAnagrams2([""]))
    print(Solution().groupAnagrams2(["a"]))

## list, dict, set : Unhashable type (mutable)
## int, str, float, tuple: Hashable type (immutable)