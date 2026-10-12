# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node,left_boundary,right_boundary):
            if not node:
                return True
            
            if not(left_boundary < node.val < right_boundary):
                return False
            
            left_is_valid = validate(node.left,left_boundary,node.val)

            right_is_valid = validate(node.right,node.val,right_boundary)

            return left_is_valid and right_is_valid
        
        return validate(root,float('-inf'),float('inf'))
