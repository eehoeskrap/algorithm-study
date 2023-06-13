
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
https://leetcode.com/problems/delete-nodes-and-return-forest/solutions/345009/python-bfs-solution/
https://leetcode.com/problems/delete-nodes-and-return-forest/solutions/934784/python-3-82-16-faster-dfs-solution/


In this problem, if the value of the node belongs to to_delete while repeatedly accessing the node, the node must be deleted.  
Also, this problem solves using DFS(Depth First Search)
It's best to convert it to a set to do O(1) lookup.

'''
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        res = []
        
        to_delete = set(to_delete)

        def helper(node):

            if not node:
                return None

            node.left = helper(node.left)
            node.right = helper(node.right)

            if node.val in to_delete:
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
                return None
            return node 

        helper(root)

        if root.val not in to_delete:
            res.append(root)
        return res 
                