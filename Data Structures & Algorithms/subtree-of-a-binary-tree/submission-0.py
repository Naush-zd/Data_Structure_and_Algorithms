# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, t: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        if not s :
            return True
        if not t:
            return False
        if self.isSame(t,s):
            return True
        return (self.isSubtree(t.left,s) or (self.isSubtree(t.right,s)))
        
    def isSame(self, t: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        if not t and not s:
            return True
        if t and s and t.val == s.val:
            return self.isSame(t.left, s.left) and self.isSame(t.right,s.right)
        return False 