# -*- coding: utf-8 -*-

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
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

    result = Solution().mergeKLists(listnode)

    # 출력
    while isinstance(result, ListNode):
        print(result.val)
        result = result.next
