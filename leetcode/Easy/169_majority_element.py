'''
https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150

모든 요소들 중에서 주로 나오는 요소를 찾는 문제
주로 나오는의 조건은 nums 배열이 주어졌을 때 nums 배열의 개수는 n이고, (n/2) 이상 나오는 수를 나타냄 
나는 set 내장 함수를 이용해서 중복을 일단 제거하고, 존재하는 요소들의 개수가 len(nums)/2 이상이면 값을 반환함 

하지만 이런 방식을 사용하게 될 경우, 
배열에서 가장 마지막에 있는 숫자가 majorityElement 라면 느리게 찾을 수 있음. 

굳이 중복을 제거하지 않더라도, 배열 내에서 주된 숫자의 개수는 반절을 넘는다고 하니까 
그냥 sorted 하여 반에 해당하는 값을 리턴해도 될 거 같다. 
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # solution 1 
        # set_nums = set(nums)
        # for set_num in set_nums:
        #     if nums.count(set_num) > (len(nums)/2):
        #         return 
            
        # solution 2 
        return sorted(nums)[len(nums)/2]