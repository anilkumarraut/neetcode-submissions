# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        arr = []
        while list1:
            arr.append(list1)
            list1 = list1.next
        
        while list2:
            arr.append(list2)
            list2 = list2.next
        
        arr.sort(key=lambda node:node.val)

        for i in range(len(arr)-1):
            arr[i].next = arr[i+1]

        return arr[0]


            


        