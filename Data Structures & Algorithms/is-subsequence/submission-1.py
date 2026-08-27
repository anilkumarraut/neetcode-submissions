class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # for i in s:
        #     for j in t:
        #         if i == j:
        #             continue
        #         return True
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)