# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def sol(node):

            if node.next is None:
                return node

            if node.next.next is None:
                node.next.next = node
                print("made", node.next.val, "head")
                n = node.next
                node.next = None
                return n
            
            else:
                n = sol(node.next)
                node.next.next = node
                print(node.next.val, "now points to", node.val)
                node.next = None
                print(n.val, "head")
                return n
        if head is None:
            return None
        return sol(head)