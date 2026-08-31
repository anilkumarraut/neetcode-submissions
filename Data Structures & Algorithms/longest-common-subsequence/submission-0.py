class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        
        # NO +1 here — exact size, no padding row/column
        dp = [[0 for j in range(n)] for i in range(m)]
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    # need dp[i+1][j+1] — but i+1 or j+1 might be OUT OF BOUNDS now!
                    diag = dp[i+1][j+1] if i+1 < m and j+1 < n else 0
                    dp[i][j] = 1 + diag
                else:
                    # need dp[i][j+1] and dp[i+1][j] — both might be out of bounds too!
                    right = dp[i][j+1] if j+1 < n else 0
                    down = dp[i+1][j] if i+1 < m else 0
                    dp[i][j] = max(right, down)
        
        return dp[0][0]