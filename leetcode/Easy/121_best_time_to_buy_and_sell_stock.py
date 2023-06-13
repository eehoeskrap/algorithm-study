'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150

test case [7,1,5,3,6,4]가 있을 때
주식 가격이 1일 때 사서 6일 때 파는게 가장 수익이 크다. 
단 여기서 주의해야할 점은 배열 순서가 날짜 순서이기 때문에 뒤로 갈수는 없다. 
따라서 인덱스를 오른쪽으로 점차 옮겨 가면서
7과 나머지 오른쪽을 비교하고
그 다음 1과 나머지 5부터 4까지 비교하고 
그 다음 5와 나머지 3부터 4까지 비교하고 이런식으로 진행되어야 한다. 
진행 될 때 마다 현재 샀다고 가정했을 때 산 가격이 오른쪽 가격보다 작다면, 즉 오른쪽 가격이 더 크다면 수익을 낼 수 있으므로
profit을 계산한다. 이 때 profit을 계산할 때 max인지 체크하는 과정을 거치면서 값을 업데이트 한다. 
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0
        left = 0
        right = 1 

        while(right < len(prices)):
            currentProfit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                profit = max(profit, currentProfit)
            else:
                left = right
            right += 1
            
        return profit