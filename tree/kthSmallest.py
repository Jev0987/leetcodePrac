# # Definition for a binary tree node.
# from typing import Optional
#
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         list = []
#         def preOrder(root):
#             if not root:
#                 return
#             list.append(root.val)
#             preOrder(root.left)
#             preOrder(root.right)
#         preOrder(root)
#
#         def rangeList(list, k):
#
#             def quickSort(list, left, right):
#                 if(left > right):
#                     return
#                 i = left - 1
#                 j = right + 1
#                 tmp = 0
#                 while True:
#                     mid = (left + right)//2
#                     while True:
#                         i += 1
#                         if list[i] >= list[mid]:
#                             break
#                     while True:
#                         j -= 1
#                         if list[j] <= list[mid]:
#                             break
#                     # while(list[++i] <= list[mid])
#                     # while(list[--j] >= list[mid])
#                     if i >= j:
#                         break
#                     tmp = list[i]
#                     list[i] = list[j]
#                     list[j] = tmp
#                 quickSort(list, left, i - 1)
#                 quickSort(list, j + 1, right)
#
#             quickSort(list, 0, len(list) - 1)
#             return list[k]
#
#         return rangeList(list, k)
#
# class Tree(object):
#     lt = []
#     def __init__(self):
#         self.root = None
#
#     def add(self, number):
#         treenode = TreeNode(number)
#
#         if self.root is None:
#             self.root = treenode
#             self.lt.append(self.root)
#         else:
#             while(True):
#                 node = self.lt[0]
#                 if node.left is None:
#                     node.left = treenode
#                     self.lt.append(node.left)
#                     return
#                 elif node.right is None:
#                     node.right = treenode
#                     self.lt.append(node.right)
#                     self.lt.pop(0)
#                     return
# def showTree(root):
#     if root is None:
#         return
#     print(root.val)
#     showTree(root.left)
#     showTree(root.right)
#
# L = [3, 1, 4, None, 2]
# L1 = []
# T = Tree()
# for i in L:
#     T.add(i)
#     print("insert successfully")
# showTree(T.root)
#
# S = Solution()
# print(S.kthSmallest(T.root, 1))

'''
    注意，是搜索树，左边一定小于根节点，一直往左能够找到最小点，从根节点不断入栈，到null时为最小点。
    最小点出栈，k-1，若k=0，输出值，若不是则将考虑右边子树，重复该操作。
'''
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
