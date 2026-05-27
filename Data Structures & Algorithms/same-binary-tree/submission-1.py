# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Time: O(n) since we are visiting 
        # Space: O(h) in the best case if height balanced 
        # 2^h = n, where n is the number of nodes. h = lg(n) / lg(2) -> lg2(n)
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            return True and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False