'''
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
'''
class Solution1(object):
    def numberOfSteps(self, num):
        step = 0
        while(num != 0):
            step += 1
            num = num // 2 if num % 2 == 0 else num - 1
        print(step)

class Solution2(object):
    def numberOfSteps(self, num):
        step = 0
        while(num != 0):
            step += 1
            if num % 2 == 0:
                num //= 2
                print(num, "is even; divide by", 2, "and obtain", num)
            else:
                num -= 1
                print(num, "is odd; divide by", 1, "and obtain", num)
        print(step)
if __name__ == "__main__":
    num = 123
    Solution1().numberOfSteps(num)
    Solution2().numberOfSteps(num)
