# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"


class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""
        resLen = 0

        for i in range(len(s)):

            # odd-length palindrom (not length of s)
            # every index is possible palindrom center (and move outward)
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:

                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1

                l -= 1
                r += 1

            # even-lenth of palindrom (not length of s)
            # every index is possible palindrom center (and move outward)
            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:

                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1

                l -= 1
                r += 1

        return res


if __name__ == "__main__":
    print(Solution().longestPalindrome("babad"))
    print(Solution().longestPalindrome("cbbd"))
    print(Solution().longestPalindrome("ac"))
    print(Solution().longestPalindrome("a"))
