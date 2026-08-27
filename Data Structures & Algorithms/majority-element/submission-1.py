class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = defaultdict(int)
        res = maxcount = 0
        for num in nums:
            ans[num] += 1
            if maxcount < ans[num]:
                res = num
                maxcount = ans[num]

        return res