# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        ans = ListNode()
        answer = ans
        nextNode = None

        while list1 is not None or list2 is not None:

            if list1 is None:
                nextNode = list2
                list2 = list2.next
            elif list2 is None:
                nextNode = list1
                list1 = list1.next
            elif(list1.val< list2.val):
                nextNode = list1
                list1 = list1.next
            else:
                nextNode = list2
                list2 = list2.next

            answer.next = nextNode
            answer=answer.next
            answer.next = None

        return ans.next
