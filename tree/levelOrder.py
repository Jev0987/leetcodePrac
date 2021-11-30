# Definition for a binary tree node.
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = list() #结果
        quene = list() #队列

        quene.append(root)

        while quene:
             cur_quene_size = len(quene)
             level = [] #每一层的元素
             while cur_quene_size > 0:
                cur_quene_size -= 1
                node = quene.pop(0)
                level.append(node.val)
                if node.left:
                    quene.append(node.left)
                if node.right:
                    quene.append(node.right)
             res.append(level)
        return res









        return res