# Definition for a binary tree node.
#先序遍历
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = list()
        def preorderf(root):
            if not root:
                return
            res.append(root.val)
            preorderf(root.left)
            preorderf(root.right)
        preorderf(root)
        return res


