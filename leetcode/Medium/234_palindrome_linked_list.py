# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
reference : https://velog.io/@changhee09/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%9F%B0%EB%84%88-%EA%B8%B0%EB%B2%95
'''
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head 
        rev = None

        # This algorithm should use the fast runner technique. 
        # fast acesses a linked list twice as fast. 
        # slow points to half of the linked list. 
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            
        # if the linked list is odd, move slow by one space, since the middle value doesn't matter. 
        if fast:
            slow = slow.next 
            
        # rev is reverse linked list of head. 
        while rev:
            if rev.val != slow.val:
                return False
            slow = slow.next
            rev = rev.next 

        return True 

            