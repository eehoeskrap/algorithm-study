class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int

        Approach:
        1. Add up all the money contained in each account.
        2. Then find the max value of account.

        Time complexity: O(n*m), n is number of account, m is number of money. 
        Space complexity: O(1)
        """
        max_value = 0
        for account in accounts:
            max_value = max(sum(account), max_value)

        return max_value