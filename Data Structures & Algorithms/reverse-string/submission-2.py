class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        for i in range(len(s)):
            stack.append(s[i])

        for i in range(len(stack)):
            s[i] = stack.pop()

        return s