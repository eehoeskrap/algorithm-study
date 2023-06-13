class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        
        https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
        nums 배열이 주어지면 val 값을 모두 제거시키고, 제거시킨 nums의 길이를 반환하는 문제 
        이 때 배열의 순서는 상관 없음. 
        
        for 문을 이용하여 풀게 될 경우 remove 할 때 마다 배열의 길이가 감소하므로 주의. 
        이럴 때는 while 문으로 nums 배열에서 val 값이 없을 때 까지 돌면서, remove 시키는게 좋음. 
        """
        # for num in nums:
        #     if num == val:
        #         nums.remove(num)

        while(nums.count(val)):
            nums.remove(val)
    
        return len(nums)
