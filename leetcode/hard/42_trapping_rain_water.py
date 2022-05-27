class Solution1(object):
    def trap(self, height):
        '''
        처음으로 생각한 방법은 아래와 같음
        블록 하나 당 층(floor)이라고 가정하고 층별로 고여있는 물(∪ 형태)을 계산하고자 하였음
        1. 오른쪽으로 이동하며 블록의 높이가 해당 층 보다 큰 경우를 만났을 때, trap_flag를 이용하여 가둘 수 있는 물의 양 카운트 시작
        2. 블록의 높이가 해당 층보다 낮거나 같은 경우 물을 가둘 수 있으므로 water += 1 시켜줌
        3. trap_flag가 true이고 블록의 높이가 해당 층보다 클 경우 현재까지 고인 물을 all_water에 더해주었음
        그 결과 318 / 321 test cases passed... 나머지는 "Time Limit Exceeded"
        '''

        all_water = 0
        for floor in range(0, max(height)):
            temp_water = 0
            trap_flag = False
            for h in height:
                if trap_flag is False and h > floor:
                    # 오른쪽으로 이동하며 처음 마주한 블록의 높이가 해당 층 보다 큰 경우 카운트 시작
                    trap_flag = True
                elif trap_flag and h > floor:
                    # 블록의 높이가 해당 층 보다 큰 경우 카운트 종료
                    if temp_water > 0:
                        all_water += temp_water
                    temp_water = 0
                elif trap_flag and h <= floor:
                    # 블록의 높이가 해당 층보다 낮거나 같은 경우 카운트
                    temp_water += 1
                else:
                    continue

        print(all_water)

class Solution2(object):
    '''
    두번째로 생각한 방법은 timeout 문제를 해결하기 위해
    solution 1 처럼 for문을 두번 돌아서 모든 height 값들에 대해 계산하는 것 보다는
    ∪ 형태의 고여있는 물을 구할 때 반으로 쪼개서 계산해야겠다는 생각을 했음
    '''

    def trap(self, height):

        # 초기화
        l = 0
        r = len(height) - 1
        left_max = height[l]
        right_max = height[r]
        all_water = 0

        # 반으로 쪼개서 생각할 때
        # ∪ 형태의 왼쪽 부분은 오른쪽으로 이동, 오른쪽 부분은 왼쪽으로 이동시키면서
        # 각 부분 이동 시 블록이 작아진다면 물이 고일 수 있으므로 그 때마다 고인 만큼 all_water를 더해줌 
        # 작아지지 않고 커지거나 같다면 업데이트 시켜줌
        while l < r:
            if height[l] < height[r]:
                # 블록이 작아지면 고인 만큼 all_water를 더해줌
                if left_max > height[l]:
                    all_water += left_max - height[l]
                else:
                    left_max = height[l]
                l += 1
            else:
                if right_max > height[r]:
                    all_water += right_max - height[r]
                else:
                    right_max = height[r]
                r -= 1

        print(all_water)


if __name__ == "__main__":

    height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    height2 = [4,2,0,3,2,5]
    height3 = [2,0,2]

    #Solution1().trap(height1)
    Solution2().trap(height1)
