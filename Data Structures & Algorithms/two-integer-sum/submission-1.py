class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indicis = {}
        for i, n in enumerate(nums):
            indicis[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indicis and indicis[diff] != i:
                return [i, indicis[diff]]
        return []