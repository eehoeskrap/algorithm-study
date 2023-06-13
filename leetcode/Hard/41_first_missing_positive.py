class Solution(object):
    def firstMissingPositive(self, nums):

        i = 0
        nums_length = len(nums)

        while i < nums_length:
            # missing positive 는 무조건 len(nums)+1 보다 작거나 같음
            if nums[i] < 1 or nums[i] > nums_length:
                # ignore
                nums[i] = 0
                i += 1
            elif nums[i] - 1 != i:
                if nums[i] == nums[nums[i] - 1]:
                    # ignore
                    nums[i] = 0
                    i += 1
                else:
                    #
                    nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1

        for i in range(nums_length):
            # ignore 된 숫자가 나오면 missing positive 반환
            if nums[i] == 0:
                return i + 1

        # 배열이 모두 탐색되었다면 len(num) + 1 반환
        return nums_length + 1

if __name__ == '__main__':

    nums = [1,2,0]
    result = Solution().firstMissingPositive(nums)
    print(result)