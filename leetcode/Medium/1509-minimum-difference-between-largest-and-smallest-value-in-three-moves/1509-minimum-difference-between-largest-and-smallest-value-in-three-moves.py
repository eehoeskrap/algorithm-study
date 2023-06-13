class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        [6,6,0,1,1,4,6]
        [0,1,1,4,6,6,6]
        [0,1,1,4,0,0,0]
        
        4-0 = 4 
        
        [0,1,1,4,2,2,2]
        
        """
        
        if len(nums) <= 4:
            return 0
        else:
            nums = sorted(nums)
            min_val = 1e10
            for a, b in zip(nums[:4], nums[-4:]):
                min_val = min(b-a, min_val)
            return min_val
            