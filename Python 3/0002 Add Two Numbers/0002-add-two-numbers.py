# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1values = []
        l2values = []

        curr = l1

        while curr:
        l1values.append(str(curr.val))
        curr = curr.next

        curr = l2

        while curr:
            l2values.append(str(curr.val))
            curr = curr.next

        l1values = l1values[::-1]
        l2values = l2values[::-1]

        l1num = int("".join(l1values))
        l2num = int("".join(l2values))

        new = str(l1num + l2num)[::-1]
        dummy = ListNode()
        curr = dummy

        for d in new:
            curr.next = ListNode(int(d))
            curr = curr.next

        return dummy.next