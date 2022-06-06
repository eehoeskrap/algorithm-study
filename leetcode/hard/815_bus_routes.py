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

if __name__ == '__main__':

    # routes = [[1, 2, 7], [3, 6, 7]]
    # source = 1
    # target = 6

    routes = [[0, 1, 6, 16, 22, 23], [14, 15, 24, 32], [4, 10, 12, 20, 24, 28, 33],
              [1, 10, 11, 19, 27, 33], [11, 23, 25, 28],[15, 20, 21, 23, 29], [29]]
    source = 4
    target = 21
    result = Solution().numBusesToDestination(routes, source, target)

    print(result)