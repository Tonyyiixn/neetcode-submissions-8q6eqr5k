class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function that takes the current node, and its allowed boundaries
        def validate(node, left_boundary, right_boundary):
            # Base case: An empty tree is a valid BST
            if not node:
                return True
            
            # Did this node break the rules passed down to it?
            if not (left_boundary < node.val < right_boundary):
                return False
            
            # Check left subtree (Update the MAX allowed value to be the current node's value)
            left_is_valid = validate(node.left, left_boundary, node.val)
            
            # Check right subtree (Update the MIN allowed value to be the current node's value)
            right_is_valid = validate(node.right, node.val, right_boundary)
            
            return left_is_valid and right_is_valid

        # Start the root with negative and positive infinity boundaries
        return validate(root, float('-inf'), float('inf'))