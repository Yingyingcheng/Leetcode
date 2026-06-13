# # Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# # An input string is valid if:

# # Open brackets must be closed by the same type of brackets.
# # Open brackets must be closed in the correct order.
# # Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Example 5:
# Input: s = "([)]"
# Output: false


class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for c in s:

            if c == "(" or c == "{" or c == "[":
                stack.append(c)

            elif stack and c == ")" and stack[-1] == "(":
                stack.pop()

            elif stack and c == "}" and stack[-1] == "{":
                stack.pop()

            elif stack and c == "]" and stack[-1] == "[":
                stack.pop()

            else:
                return False

        return not stack


if __name__ == "__main__":
    print(Solution().isValid("()"))
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("(]"))

    print(Solution().isValid("([])"))
    print(Solution().isValid("([)]"))
    print(Solution().isValid("("))
    print(Solution().isValid(""))
