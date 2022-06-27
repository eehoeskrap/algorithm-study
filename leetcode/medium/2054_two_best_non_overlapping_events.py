# -*- coding: utf-8 -*-

class Solution(object):

    def maxTwoEvents(self, events):

        answer = 0 
        # end_time 기준으로 정렬
        events.sort(key = lambda x:x[1]) 
        # events의 길이 만큼 반복연산자로 배열 할당
        maxleft = [0] * len(events)
        # end_time의 max 값 초기화 
        maxleft[0] = events[0][2] 
            
        # 초기화에 사용한 값 제외하고 for문 돌면서 value의 최대값을 maxleft에 저장 
        for i in range(1, len(events)): 
            maxleft[i] = max(maxleft[i-1], events[i][2])  

        # events 값을 binary search 수행하며
        # overlap 되지 않는 end_time 값들 중 maxleft과의 최대값을 구해줌 
        for i in range(len(events)): 
            left, right = 0, len(events)-1
            while left < right: 
                mid = left + (right-left) // 2+1 
                if events[mid][1]<events[i][0]: 
                    left = mid
                else: 
                    right = mid-1 
            # end_time 값 
            end_t = events[i][2] 

            # overlap 되지 않는 범위에 도착했을 때 left 값과 end 값을 더해줌 
            if events[right][1] < events[i][0]: 
                end_t += maxleft[right] 
            
            # max 값 저장 
            answer = max(answer, end_t) 
                
        return answer

if __name__ == '__main__':

    # startTime, endTime, value
    #events = [[1,3,2],[4,5,2],[2,4,3]]
    #events = [[1,3,2],[4,5,2],[1,5,5]]
    #events = [[1,5,3],[1,5,1],[6,6,5]]
    #events = [[10,83,53],[63,87,45],[97,100,32],[51,61,16]]
    events = [[66,97,90],[98,98,68],[38,49,63],[91,100,42],[92,100,22],[1,77,50],[64,72,97]]
    result = Solution().maxTwoEvents(events)

    print("answer", result)