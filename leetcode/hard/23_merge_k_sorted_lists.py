# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution2(object):
    def mergeKLists(self, lists):

        print("?????")
        if not lists: return None
        if len(lists) == 1: return lists[0]

        # 일단 link로 연결되어 있으니,
        # 값을 비교하면서 결과에 따라 next를 대치해주는 작업이 필요함
        # 그 전에 반으로 쪼개서 비교할 것
        mid = len(lists) // 2
        left  = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return self.merge(left, right)

    def merge(self, left, right):

        temp = ListNode()
        result = temp

        while left and right:
            if left.val < right.val:
                temp.next = left # 작은 값을 가리키게 함
                left = left.next # 원래 left 리스트의 첫번째 값을 그 다음 값으로 대치
            else:
                temp.next = right
                right = right.next
            temp = temp.next

        temp.next = left or right  # 둘 중 하나의 값만 있다면 둘 중 하나로 대입
        return result.next

class Solution1(object):
    def mergeKLists(self, lists):

        if not lists: return None
        if len(lists) == 1: return lists[0]

        sorted_lists = []
        temp = ListNode() # sorted lists를 재저장 할 ListNode 타입의 temp 선언
        result = temp     # result -> temp

        # 모든 ListNode의 값에 접근하면서 sorted_lists 배열에 담음
        for l in lists:
            while l:
                sorted_lists.append(l.val)
                l = l.next

        # 정렬
        # 만약 sort 함수를 쓰지 않는다면,
        # ListNode 값 비교하면서 새로운 ListNode 생성해내면 될듯
        sorted_lists.sort() # O(NlogN)

        # 정렬된 배열에서 값을 하나씩 ListNode로 temp에 할당하며 값을 대입
        for s_list in sorted_lists:
            temp.next = ListNode(s_list)
            temp = temp.next

        return result.next # result가 가르키는 ListNode 리턴

if __name__ == '__main__':


    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]

    # 테스트를 위해 ListNode 값을 할당 하기 위함
    listnode = []
    for list in lists:
        temp = ListNode(list[0]) # first value
        for val in list[1:]:
            temp.next = ListNode(val)
        listnode.append(temp)

    result = Solution2().mergeKLists(listnode)

    # 출력
    while isinstance(result, ListNode):
        print(result.val)
        result = result.next
