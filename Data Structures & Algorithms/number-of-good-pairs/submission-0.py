class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pair = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    pair.add(tuple((i,j)))
        return len(pair)
        