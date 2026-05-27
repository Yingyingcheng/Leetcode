# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-2 ** 31, 2 ** 31 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21

# Constraints:

# -2 ** 31 <= x <= 2 ** 31 - 1


class Solution:
    def reverse(self, x: int) -> int:
        res = ""

        for char in str(x):
            res = char + res

        if x >= 0:
            return int(res) if int(res) <= (2**31 - 1) else 0

        elif x < 0:
            return -int(res[:-1]) if -int(res[:-1]) >= -(2**31) else 0


if __name__ == "__main__":
    print(Solution().reverse(123))
    print(Solution().reverse(-123))
    print(Solution().reverse(120))
    print(Solution().reverse(0))
    print(Solution().reverse(1534236469))  ## this one is greater than 2**31 - 1
