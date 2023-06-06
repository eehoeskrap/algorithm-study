class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        if len(coins) == 1:
            if coins < amount: 
                return -1
        if amount == 0:
            return 0
        
        return res
        
           
         
           
        
        

if __name__ == "__main__":
    coins = [1,2,5]
    amount = 11
    res = Solution().coinChange(coins, amount)
    print(res)
        