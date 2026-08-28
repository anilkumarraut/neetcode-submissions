class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0] * n
        prefixSum[0] = nums[0]

        for i in range(1, n):
            prefixSum[i] = prefixSum[i-1] + nums[i]

        for i in range(n):
            leftSum = 0 if i == 0 else prefixSum[i-1]
            rightSum = prefixSum[n-1] - prefixSum[i]
            if leftSum == rightSum:
                return i

        return -1