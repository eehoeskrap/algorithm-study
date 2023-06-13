class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        26. Remove Duplicates from Sorted Array의 업그레이드 버전 
        https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150

        non-decreasing order 인 배열 nums이 주어지면, 존재하는 num 마다 "최대 2개씩" 남기고 중복을 제거한다. 
        26번 문제와 마찬가지로 중복 제거라는 것은 존재하는 숫자가 최대 1개여야한다. 
        이 문제에서는 최대 2개까지만 남기라고 했으므로, num 마다 최대 2개씩이 될 때까지 remove 한다. 
        이 때 1개만 존재하는 숫자도 있을 수 있기 때문에 if 문을 통해 1개일 경우 remove를 하지 않고 종료한다. 
        
        """

        for num in nums:
            while(nums.count(num) != 2):
                if nums.count(num) == 1:
                    break
                nums.remove(num)

        return len(nums)
