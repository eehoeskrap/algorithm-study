class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        
        Approach (=> Time Limit Exceeded)
        1. First, Remove duplicate number.
        2. Count the numbers that appear more than once.
        3. If a number appears more than once, it is returned "True" immediately.
        4. Otherwise, return "False".

        Approach 
        1. Compare the length of the deduplicated number with the length of the input. 

        Time Complexity : O(1)
            Python's len() automatically increments when data is defined and saved.
            Then, returns the stored value.
            Python's set() operates as long as the length of the data. Big O of set() is O(len(N))

        Space Complexity : O(1)
        """

        # set_nums = set(nums)
        # for num in set_nums:
        #     if nums.count(num) >= 2:
        #         return True

        # return False

        return len(nums) != len(set(nums))


        

        