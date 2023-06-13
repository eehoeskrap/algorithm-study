# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
The problem was solved using DFS(Depth First Search)

Time Complexity : O(N), N is the number of nodes in the tree
Space Complexity : O(N)

'''
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        
        self.sum = 0
        self.dfs(root, low, high)
        return self.sum 
    
    
    def dfs(self, root, low, high):
        if root == None:
            return None
        
        if low <= root.val and root.val <= high:
            self.sum += root.val
            
        if low < root.val:
            self.dfs(root.left, low, high)
            
        if high > root.val:
            self.dfs(root.right, low, high)
            
        
        