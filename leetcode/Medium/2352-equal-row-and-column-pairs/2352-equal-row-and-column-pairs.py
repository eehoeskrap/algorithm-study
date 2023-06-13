class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        
        Approach 1.
        Time Complexity : O(N^3) (It is not best.)
        Space Complexity : O(N)

        cnt = 0

        for i in range(len(grid)):
            v_string = grid[i]
            for z in range(len(grid)):
                h_string = []
                for j in range(len(grid)):
                    h_string.append(grid[j][z])
                if h_string == v_string:
                    cnt += 1 

        return cnt 
        """
        
        '''
        Approach 2. 
        Hash Map 
        
        Save row's value and number of row's value 
        There is no comparison. 
        Implementation without using collections.Counter.
        
        Time Complexity : O(N^2)
        Space Complexity : O(N)
        '''

        row_counter = {}
        for row in grid:
            row_counter[tuple(row)] = grid.count(row)
        
        print(row_counter)
        cnt = 0 
        for i in range(len(grid)):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
                if tuple(col) in row_counter.keys():
                    cnt += row_counter[tuple(col)]

        return cnt 
    
    
        '''
        Approach 3. 
        Hash Map 
        
        Implementation without using collections.Counter.
        
        Time Complexity : O(N^2)
        Space Complexity : O(N)
        '''
#         count = 0
#         n = len(grid)
        
#         row_counter = collections.Counter(tuple(row) for row in grid)
#         for c in range(n):
#             col = [grid[i][c] for i in range(n)]
#             count += row_counter[tuple(col)]
#         print(row_counter )
#         return count 
    
    
        