# -*- coding: utf-8 -*-
from collections import deque
class Solution(object):
    def numBusesToDestination(self, routes, source, target):

        if source == target : return 0

        # 각 정류장에서 탈 수 있는 모든 버스 저장
        # e.g. 7번 정류장 : 0번 버스, 1번 버스
        #      {1: [0], 2: [0], 3: [1], 6: [1], 7: [0, 1]}
        stop_dict = {}
        for bus, stops in enumerate(routes):
            for stop in stops:
                if stop not in stop_dict:
                    stop_dict[stop] = [bus]
                else:
                    stop_dict[stop].append(bus)

        queue = deque([source])

        # 이 전에 탔던 버스를 체크
        visited = set()

        result = 0
        while queue:
            result += 1
            pre_num_stops = len(queue)
            for _ in range(pre_num_stops):
                cur_stop = queue.popleft()
                for bus in stop_dict[cur_stop]:
                    if bus in visited: continue
                    visited.add(bus)
                    for stop in routes[bus]:
                        if stop == target: return result
                        queue.append(stop)
        return -1

class Solution1(object):
    def numBusesToDestination(self, routes, source, target):

        if source == target : return 0

        # 각 정류장에서 탈 수 있는 모든 버스 저장
        # e.g. 7번 정류장 : 0번 버스, 1번 버스
        #      {1: [0], 2: [0], 3: [1], 6: [1], 7: [0, 1]}
        stop_dict = {}
        for bus, stops in enumerate(routes):
            for stop in stops:
                if stop not in stop_dict:
                    stop_dict[stop] = [bus]
                else:
                    stop_dict[stop].append(bus)

        print(stop_dict)
        queue = deque([source])
        #queue = [source]
        '''
        deque는 앞뒤로 원소를 뺄 수 있는 자료구조이며, 
        popleft로 앞에 있는 원소를 뺄 수 있음
        그렇다면 일반 리스트에서 pop(0)과 어떤 차이가 있는가?
        일반 리스트에서는 리스트의 크기에 따라 읽어오는 시간이 달라짐 즉 O(N)이 걸림
        하지만 deque의 popleft를 사용할 경우에는 O(1)의 시간이 걸림 
        '''
        # 이 전에 탔던 버스를 체크
        visited = set()
        '''
        set은 언제 사용하면 좋을까
        1. 삽입과 동시에 정렬이 필요할 때
        2. 중복을 제거한 원소의 집합이 필요할 때
        3. 현재 원소가 중복된 값인지 확인이 필요할 때
        '''


        result = 0
        while queue:
            result += 1 # 버스 탑승
            pre_num_stops = len(queue)
            for _ in range(pre_num_stops):
                cur_stop = queue.popleft() # 현재 머문 정류장
                for bus in stop_dict[cur_stop]: # 현재 정류장의 버스 중에서
                    if bus in visited: continue # 해당 버스를 탄적이 있다면 계속 진행ㅇ
                    visited.add(bus)
                    for stop in routes[bus]:
                        if stop == target: return result
                        queue.append(stop)

                        print(queue)

        return -1



if __name__ == '__main__':

    routes = [[1, 2, 7], [3, 6, 7]]
    source = 1
    target = 6

    # routes = [[0, 1, 6, 16, 22, 23], [14, 15, 24, 32], [4, 10, 12, 20, 24, 28, 33],
    #           [1, 10, 11, 19, 27, 33], [11, 23, 25, 28],[15, 20, 21, 23, 29], [29]]
    # source = 4
    # target = 21
    result = Solution1().numBusesToDestination(routes, source, target)
