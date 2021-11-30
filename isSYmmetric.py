# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#参考leetcode的解答方式
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        #对比判断左子树左边和右子树右边节点，左子树右边节点和右子树左边节点
        def isSymmetricHelper(L, R):
            #边界条件，左右子树节点对称相等且不为空
            if not L and not R:
                return True
            #左右子树对应节点有值且相等
            if L and R and L.val == R.val:
                #左子树左节点和右子树右节点做对比，左子树右节点和右子树左节点做对比
                return isSymmetricHelper(L.left, R.right) and isSymmetricHelper(L.right, R.left)
            return False
        return isSymmetricHelper(root, root)
