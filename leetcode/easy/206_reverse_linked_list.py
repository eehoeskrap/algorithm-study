# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
References : https://underdog11.tistory.com/78
'''
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev = None # It is a final result for save previous value.
        curr = head # curr is value of current location.

        while curr: # Iteration until curr is None. 
            next = curr.next # next points to next of curr  
            curr.next = prev # frist, curr.next points to the None value, then to the previous value. 
            prev = curr # then, prev points to curr 
            curr = next # Move the curr value to the next value. 
    
        return prev 