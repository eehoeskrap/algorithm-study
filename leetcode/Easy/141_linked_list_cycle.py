# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


'''
방문했던 리스트나 배열을 생성하여 
연결 리스트를 끝날 때 까지 순회하면서 
방문했던 노드들을 저장하고, 방문할 때마다 노드들을 방문했었는지 체크하면 됨 
그리고 while 문 조건을 head.next != None 이라고 두게되면, 
NoneType은 next가 없다고 뜸 
또한 dict에 head를 저장할 때도 head.val을 저장하는게 아니라 head 전체를 저장해야함 
'''
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # 19 / 23 testcases passed
        # [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]

        # dictionary = {} 
        # while(head.next != None):
        #     if head.val in dictionary:
        #         return True
        #     else:
        #         dictionary[head.val] = True 

        #     head = head.next

        # return False

        dictionary = {} 
        while(head):
            if head in dictionary:
                return True
            else:
                dictionary[head] = True 

            head = head.next

        return False