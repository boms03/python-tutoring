class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.mirror(root.left, root.right) 
    def mirror(self,left,right):
        if not left and not right:
            return True 
        if not left or not right:
            return False
        if left.val!=right.val:
            return False 
        return self.mirror(left.left, right.right) and self.mirror(left.right, right.left)



   
