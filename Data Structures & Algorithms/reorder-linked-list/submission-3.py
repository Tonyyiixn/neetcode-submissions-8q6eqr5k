# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        list1 = slow.next
        slow.next = None 
        prev = None

        while list1:
            tmp = list1.next
            list1.next = prev
            prev = list1
            list1 = tmp
        
        list2 = head
        list1 = prev
        while list1:
            tmp1 = list1.next
            tmp2 = list2.next
            list2.next = list1
            list1.next = tmp2
            list1 = tmp1
            list2 = tmp2
        
        