class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        start = 0
        end = len(height) - 1
        result = 0

        # 일단 처음에 마주한 기둥과 제일 마지막 기둥을 이용해서 계산 가능한 면적(기둥이 낮은 쪽)을 구하고, 
        # 그 다음 start, end point가 서로 만날 때 까지 각 point를 움직이면서 면적을 구함
        while start <= end:
            # start point와 end point 사이에서 계산 가능한 면적을 구함
            area = min(height[start], height[end]) * (end - start)
            # 최대로 생성할 수 있는 면적인지 체크 
            result = max(result, area)
        
            # 기둥의 높이가 작은 쪽 기준으로 물을 채울 수 있으니까
            # 기둥의 높이가 작은 쪽으로 point를 옮김
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1 


        return result
            

if __name__ == '__main__':

    height = [1,8,6,2,5,4,8,3,7]
    #height = [1,1]
    result = Solution().maxArea(height)

    print("result", result)