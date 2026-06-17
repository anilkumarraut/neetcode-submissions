
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 1. Create an empty list to act as our min-heap
        min_heap = []
        
        # 2. Iterate through every number in the array
        for num in nums:
            # Push the current number into the heap
            heapq.heappush(min_heap, num)
            
            # If the heap size exceeds k, pop the smallest element out
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
        # 3. The root of the heap is now the kth largest element
        return min_heap[0]
