# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree(object):
    lt = []#存放左右节点未满的点
    def __init__(self):
        self.root = None

    def add(self, number):
        #创建节点
        treeNode = TreeNode(number)
        if self.root is None:
            self.root = treeNode
            Tree.lt.append(self.root)
        else:
            while(True):
                node = Tree.lt[0]
                if node.left is None:
                    node.left = treeNode
                    Tree.lt.append(node.left)
                    return
                elif node.right is None:
                    node.right = treeNode
                    Tree.lt.append(node.right)
                    Tree.lt.pop(0)#左右都满了，从未满列表中删除
                    return

def showTree(Tree):
    if Tree is None:
        return
    print(Tree.val)
    showTree(Tree.left)
    showTree(Tree.right)

'''
    刚开始访问根节点，并且减去该点值
    不断递归遍历（树的遍历），并且减去对应节点值，得到一个剩余数值
    若到叶子节点时剩余数值不为0，返回上一层位置
'''

'''
    本题小结，刚开始的递归关系找的辛苦，后面的判断条件在返回True时考虑不周。多注意“结果完美，返回True”那个条件：如在什么时候进入这个判断，为什么要这么判断，逻辑要清晰
'''
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if root is None and targetSum == 0:
            return False

        def PathSumHelper(root, leftSum):

            # 访问到叶子节点，但是不能完整减去
            if root is None:
                return False

            # 结果完美，返回True
            if root.left is None and root.right is None and leftSum - root.val == 0:
                return True

            # # 剩下的值已经为0，但是不是叶子节点
            # if leftSum == 0 and root is not None:
            #     return False

            return PathSumHelper(root.left, leftSum - root.val) or PathSumHelper(root.right, leftSum - root.val)



        return PathSumHelper(root, targetSum)


L = [1,2,3]
L1 = [5,4,8,11,0,13,4,7,2,0,0,0,1]
L2 = [1, 2]
T = Tree()
for i in L1:
    T.add(i)
    print("添加节点成功")

showTree(T.root)
S = Solution()
print(S.hasPathSum(T.root, 22))

