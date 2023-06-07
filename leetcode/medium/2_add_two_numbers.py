# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
https://leetcode.com/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-interview-150
연결 리스트로 순회하면서 푸는 문제
자리수는 자리수 만큼 10의 자리를 곱해줌으로써 숫자를 완성했음
그 다음 숫자를 string으로 만들어주고, string을 거꾸로 부터 연결리스트 만들어줌 
'''
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l1_digit = 0
        mul = 1
        while(l1):
            l1_digit += l1.val * mul
            l1 = l1.next 
            mul *= 10

        l2_digit = 0
        mul = 1
        while(l2):
            l2_digit += l2.val * mul
            l2 = l2.next 
            mul *= 10

        l3_digit = str(l1_digit + l2_digit)

        head = l3 = ListNode(l3_digit[len(l3_digit)-1])
        for i in range(len(l3_digit)-2, -1, -1):
            l3.next = ListNode(l3_digit[i])
            l3 = l3.next 
        return head


