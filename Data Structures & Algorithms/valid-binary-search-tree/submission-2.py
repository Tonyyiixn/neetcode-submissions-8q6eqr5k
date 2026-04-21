# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.validate(root,float('-inf'),float('inf'))

    def validate(self,node,low,high):
        # 1. Base Case: An empty node is always valid
        if not node:
            return True

        # 2. Check the Current Node
        # If node.val is NOT strictly between low and high... return False
        if node.val <= low or node.val >=high:
            return False
        # 3. Recursion: Check Left and Right
        # Left child: Must be > low AND < node.val
        # Right child: Must be > node.val AND < high
        return self.validate(node.left,low,node.val) and  self.validate(node.right,node.val,high)