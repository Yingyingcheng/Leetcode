# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?


# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


## Using my familiar one DP (Bottom - Up)
class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [0] * (n + 1)  ## n = 5, dp = [0, 0, 0, 0, 0, 0]

        if n < 2:
            return n

        dp[0], dp[1] = 1, 1

        for i in range(2, n + 1):

            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


## Using DP (Top-Down like tree)
class Solution1:
    def climbStairs(self, n: int) -> int:

        cache = [-1] * (n + 1)

        def dfs(i):

            if i >= n:
                return i == n  ## return true(1) if i == n or false(0)

            if cache[i] != -1:
                return cache[i]

            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]

        return dfs(0)


if __name__ == "__main__":
    print(Solution().climbStairs(2))
    print(Solution().climbStairs(3))
    print(Solution().climbStairs(5))
    print(Solution1().climbStairs(2))
    print(Solution1().climbStairs(3))
    print(Solution1().climbStairs(5))
