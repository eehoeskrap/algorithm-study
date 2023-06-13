# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        
        ############################################ list1, list2 생성 코드 
        
        l_1 = [1,2,4]
        l_2 = [1,3,4]

        # 이런식으로 삽입하게 되면, list1에 1개의 값만 저장됨 
        # list1 = ListNode(l_1[0])
        # for i in range(1, len(l_1)):
        #     list1 = ListNode(l_1[i])
        #     list1.next = list1

        # 이런식으로 대입하거나 
        # list1=ListNode(1)
        # list1.next=ListNode(2)
        # list1.next.next=ListNode(4)

        # 아래와 같이 대입해야함
        list1 = list11 = ListNode(l_1[0])
        for i in range(1, len(l_1)):
            list11.next = ListNode(l_1[i])
            list11 = list11.next
        list11 = list11.next # 마지막 값을 삽입해야함 

        list2 = list22 = ListNode(l_2[0])
        for i in range(1, len(l_2)):
            list22.next = ListNode(l_2[i])
            list22 = list22.next
        list22 = list22.next # 마지막 값을 삽입해야함 
            
        # while(list1):
        #     print(list1.val)
        #     list1 = a.next
        
        ############################################ list1, list2 생성 코드 
        
        # initial 
        dummy = cur = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next        # cur 가 다음 값을 가르키도록 업데이트 
        cur.next = list1 or list2 # 둘 중 남아있는 값 저장 (두 개의 리스트 중 하나가 비어있을 때를 위한 예외처리)

        return dummy.next 
