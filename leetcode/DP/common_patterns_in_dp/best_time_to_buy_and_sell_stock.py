class Solution(object):

    def maxProfit(self,prices):
        
        '''
        status : buy, sell, cooldown(doing nothing)
        
        i : i-th (day)
        buy : -prices[i]
        sell : +prices[i]
        cooldown : 0 
        '''
        
        if len(prices) == 1:
            return 0
                    
        stock = [0] * (len(prices) + 1)   
        money = [0] * (len(prices) + 1)
        
        # init  
        stock[1] = -prices[0]
        money[1] = 0
            
        for i in range(1, len(prices)):
            stock[i+1] = max(stock[i], money[i-1] - prices[i])
            money[i+1] = max(stock[i] + prices[i], money[i])
            
        return money[len(prices)]
        

if __name__ == "__main__":
    prices1 = [1,2,3,0,2]
    prices2 = [1, 2]
    res = Solution().maxProfit(prices2)
    print(res)
