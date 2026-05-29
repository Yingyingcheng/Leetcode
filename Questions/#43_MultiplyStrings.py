# Given two non-negative integers num1 and num2 represented as strings,
# return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.


# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"

# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"


# Constraints:
# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.


class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"

        l1, l2 = len(num1), len(num2)
        res = [0] * (l1 + l2)
        num1, num2 = num1[::-1], num2[::-1]
        for i2 in range(l2):
            for i1 in range(l1):

                digit = int(num2[i2]) * int(num1[i1])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10

        res, start_index = res[::-1], 0
        while start_index < len(res) and res[start_index] == 0:
            start_index += 1

        res = map(str, res[start_index:])
        return "".join(res)


if __name__ == "__main__":
    print(Solution().multiply("2", "3"))
    print(Solution().multiply("123", "456"))
    print(Solution().multiply("120", "0"))
