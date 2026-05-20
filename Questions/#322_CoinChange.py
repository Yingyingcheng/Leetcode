# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.


# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0


from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ## Create a DP array dp where dp[a] = minimum coins needed to make amount a
        ## [1, 3, 4, 5] amount = 7
        ## dp     =  [__,__,__,__,__,__,__,__,__] with value (greater than 1 * amount)
        ## amount =>  0, 1, 2, 3, 4, 5, 6, 7, 8

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):  ## a = 7

            for coin in coins:  ## 1, 3, 4, 5

                if (a - coin) >= 0:  ## dp[7] = min(dp[7], 1 + dp[6] )

                    dp[a] = min(dp[a], 1 + dp[a - coin])

        return dp[amount] if dp[amount] != amount + 1 else -1


if __name__ == "__main__":
    print(Solution().coinChange([1, 2, 5], 11))
    print(Solution().coinChange([2], 3))
    print(Solution().coinChange([1], 0))
    print(Solution().coinChange([1, 3, 4, 5], 7))
