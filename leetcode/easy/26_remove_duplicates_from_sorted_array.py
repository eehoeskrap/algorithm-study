class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150
       
        non-decreasing order 방식을 가지는 배열 nums이 주어지면, 여기서 중복을 제거하고, 
        in-place 방식으로 진행하여 nums의 길이를 반환하는 문제 
        
        이 때 중복 제거라는 것은 최소 num 마다 1개의 값은 잔존해야되므로, 
        for 문으로 nums 개수만큼 돌면서, while 문을 이용하여 nums의 개수가 1개가 될 때 까지 remove 시켜준다. 
        """
        
        for num in nums:
            while(nums.count(num)!=1):
                nums.remove(num)

        return len(nums)
