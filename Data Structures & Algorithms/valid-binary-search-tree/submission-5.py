# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node,left_boundry,right_boundry):
            if not node:
                return True
            
            if not (left_boundry < node.val < right_boundry):
                return False
            
            return validate(node.left,left_boundry,node.val) and validate(node.right,node.val,right_boundry) 
        
        return validate(root,float('-inf'),float('inf'))
            
            