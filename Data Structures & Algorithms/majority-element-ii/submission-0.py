class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        n = len(nums)
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        return [num for num, c in count.items() if c > n // 3]