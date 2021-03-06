# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

# Return true if and only if the nodes corresponding to the values x and y are cousins.

 

# Example 1:


# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
# Example 2:


# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
# Example 3:



# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
 

# Note:

# The number of nodes in the tree will be between 2 and 100.
# Each node has a unique integer value from 1 to 100.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_info=[]
        y_info=[]
        depth=0
        if root is None:
            return False
        self.dfs(root,x,y,0,None,x_info,y_info)
        return x_info[0][0]==y_info[0][0] and x_info[0][1]!=y_info[0][1]
    
    def dfs(self,root,x,y,depth,parent,x_info,y_info):
        if root is None:
            return None
        if root.val==x:
            x_info.append((depth,parent))
        if root.val==y:
            y_info.append((depth,parent))
        
        self.dfs(root.left,x,y,depth+1,root,x_info,y_info)
        self.dfs(root.right,x,y,depth+1,root,x_info,y_info)