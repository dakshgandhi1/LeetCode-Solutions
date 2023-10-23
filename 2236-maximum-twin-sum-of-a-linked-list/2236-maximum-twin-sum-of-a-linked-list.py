# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        n = 0
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            n+=1
        s = [0]*n
        i = 0
        while slow:
            s[i] = s[i] + head.val
            s[n-i-1] = s[n-i-1] + slow.val
            head = head.next
            slow = slow.next
            i+=1

        return max(s)