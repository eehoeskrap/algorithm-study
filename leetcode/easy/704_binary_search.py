''' 
문제 : https://leetcode.com/problems/binary-search
'''

class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while(left <= right):
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                # target 숫자가 현재 위치보다 작으면 오른쪽 search
                right = pivot - 1
            else:
                # target 숫자가 현재 위치보다 크면 왼쪽 search
                left = pivot + 1
        return -1
