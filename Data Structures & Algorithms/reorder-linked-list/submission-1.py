# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1 convert to array then use two pointer to make the array from the begining and End
        if not head or not head.next:
            return
        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next

        n = len(arr)
        l, r = 0, n-1
        
        while l < r:
            arr[l].next = arr[r]
            l += 1
            if l == r:
                break
            arr[r].next = arr[l]
            r -= 1

        arr[l].next = None
