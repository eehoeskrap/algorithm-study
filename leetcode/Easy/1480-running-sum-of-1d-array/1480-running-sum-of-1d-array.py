class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        Solution 1. 
        This problem was solved using array and sum. 
        The time complexity is O(N). 
        The space complexity is O(len(nums)). 

        Solution 2. 
        This problem was solved in-place. 
        The time complexity is O(N).
        The space complextiy is O(1).
        """

        # res = []
        # sum = 0 
        # for num in nums:
        #     sum += num 
        #     res.append(sum)

        # return res 

        i = 1 
        while i < len(nums):
            nums[i] += nums[i-1]
            i += 1
        return nums 
        