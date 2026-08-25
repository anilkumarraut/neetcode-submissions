class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for nun in nums:
            if nun in seen:
                return nun
            seen.add(nun)
        return -1
        