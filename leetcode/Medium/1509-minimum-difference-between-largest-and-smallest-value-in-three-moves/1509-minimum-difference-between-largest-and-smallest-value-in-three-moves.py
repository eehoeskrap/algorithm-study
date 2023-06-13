class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        """
        # 리스트가 4개 이하라면, 나머지 3개 값을 기준 값 1개로 전부 채우면 되기 때문에 항상 0
        if len(nums) <= 4:
            return 0
        else:
            nums = sorted(nums)
            
            # min_val 값을 초기화 하고, 정렬된 리스트에서 앞에 4개 값과 뒤에 4개 값으로 만들 수 있는 b-a 수 중에서 최소 값을 반환 
            # min_val = 1e10 
            # for a, b in zip(nums[:4], nums[-4:]):
            #     min_val = min(b-a, min_val)
            # return min_val

            # minval 값을 설정하지 않고도 한 줄로 해결 가능 
            return min(b-a for a, b in zip(nums[:4], nums[-4:]))
            