class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
      
        # sort 함수가 없었더라면?
        sum_nums = nums1 + nums2
        sum_nums.sort()
        n = len(sum_nums)
        m = int(n/2)

        if n % 2 == 0:
            # 2.0 대신 2를 쓰는 바람에 Wrong Answer 떴었음 
            result = (sum_nums[m - 1] + sum_nums[m]) / 2.0 
        else:
            result = sum_nums[m]

        # 아래와 같이 한 줄로 쓰는 것도 가능하지만 가독성이 매우 좋지 않음
        # result = (sum_nums[m - 1] + sum_nums[m]) / 2.0 if n % 2 == 0 else sum_nums[m]

        return result

if __name__ == "__main__":
    #nums1 = [1, 3]
    #nums2 = [2]
    nums1 = [1, 2]
    nums2 = [3, 4]
    Solution().findMedianSortedArrays(nums1, nums2)
