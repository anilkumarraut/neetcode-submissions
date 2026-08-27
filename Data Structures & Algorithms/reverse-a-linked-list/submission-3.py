# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        # Step 1: collect all nodes into an array
        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
        
        # Step 2: reverse the array order
        arr = arr[::-1]
        
        # Step 3: re-link nodes in the new (reversed) order
        for i in range(len(arr) - 1):
            arr[i].next = arr[i + 1]
        
        arr[-1].next = None   # last node in reversed order must point to None
        
        return arr[0] 