# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        sum_of_heads = 0
        head = None
        cur = None

        while sum_of_heads > 0 or l1 or l2:
            
            v1 = 0
            v2 = 0

            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next

            sum_of_heads += v1 + v2

            if not head:
                head = ListNode(sum_of_heads%10)
                cur = head
            else:
                cur.next = ListNode(sum_of_heads%10)
                cur = cur.next


            sum_of_heads //= 10


        return head