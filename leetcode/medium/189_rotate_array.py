'''
https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150

k 만큼 1차원 배열을 회전 시키는 문제 
처음에는 append 또는 insert를 통해서 배열 사이즈를 임의로 늘린 다음에 
늘린 공간에 마지막 배열 원소를 대입하고, remove를 반복하는 식으로 진행했음
즉, temp 공간을 임의로 만들어서 삽입 삭제를 반복함. 
time limit exceed 일어남, space complexity가 늘어남. BigO(N)

그래서 solution을 참고한 결과
k 개수를 len(nums)으로 나눠 반으로 쪼갤 기준 점 k를 구한 다음, 
k로 쪼갠다. 쪼개진 왼쪽 부분에 대해 맨 첫번째 값과 맨 나중 값을 바꾸고
그 다음 두번째 값과 맨 나중 값의 전에 있는 값을 바꾼다. 
이런 식으로 쪼개진 오른쪽 부분에 대해 진행. 
그 다음 각 왼쪽, 오른쪽에 대해 swap 작업이 완료 되었으면,
최종 결과를 위해 0번과 len(nums)-1번째를 swap 시키고,
1번과 len(nums)-2번을 swap 시키는 등 
왼쪽의 index가 오른쪽의 index 보다 같거나 커질 때 까지만 반복한다.  

'''

class Solution(object):

    def reverse(self, nums, i, j):
        li = i
        ri = j

        while li < ri:
            temp = nums[li]
            nums[li] = nums[ri]
            nums[ri] = temp

            li += 1
            ri -= 1 


    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # Time Limit Exceeded, 36 / 38 testcases passed
        # for i in range(k):
        #     nums.append(nums[0])
        #     nums[1:] = nums[:len(nums)-1]
        #     nums[0] = nums[len(nums)-1]
        #     nums.pop()

        # Time Limit Exceeded, 37 / 38 testcases passed
        # for i in range(k):
        #     nums.insert(0, nums[len(nums)-1])
        #     nums.pop()

        # 최적화된 방법
        # https://leetcode.com/problems/rotate-array/solutions/1730142/java-c-python-a-very-very-well-detailed-explanation/
        # Time Complexity  : BigO(N)
        # Space Complexity : BigO(1)
        k = k % len(nums) # 반으로 쪼갬
        if k < 0:
            k += len(nums)
        
        self.reverse(nums, 0, len(nums)-k-1) # 왼쪽에 해당하는 부분  
        self.reverse(nums, len(nums)-k, len(nums)-1) # 오른쪽에 해당하는 부분
        self.reverse(nums, 0, len(nums)-1) # 전체 리버스  

