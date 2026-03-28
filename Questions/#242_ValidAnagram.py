# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

from collections import defaultdict
from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


class Solution1:
    def isAnagram1(self, s: str, t: str) -> bool:
        S = defaultdict(int)
        T = defaultdict(int)


        for char in s:
            if char not in S:
                S[char] = 1

            else:
                S[char] += 1

        for char in t:
            if char not in T:
                T[char] = 1

            else:
                T[char] += 1


        for k1 in S:
            
            if S[k1] != T[k1] or k1 not in T:
                return False
        
        for k2 in T:
            if T[k2] != S[k2] or k2 not in S:
                return False

        return True
    

if __name__ == "__main__":
    print(Solution().isAnagram("anagram", "nagaram"))
    print(Solution().isAnagram("rat", "car"))
    print(Solution1().isAnagram1("anagram", "nagaram"))
    print(Solution1().isAnagram1("rat", "car"))
