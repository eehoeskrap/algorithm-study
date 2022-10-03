class Solution(object):

    def tribonacci(self,n):
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        elif n >= 3:
            tribo = [0] * (n+1)
            tribo[0] = 0
            tribo[1] = 1
            tribo[2] = 1
            i = 3
            while i <= n:
                tribo[i] = tribo[i-1] + tribo[i-2] + tribo[i-3]
                i += 1
            return tribo[n]

if __name__ == "__main__":
    n = 25
    res = Solution().tribonacci(n)
    print(res)