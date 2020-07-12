#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder = deque(preorder)
        return self.getTree(preorder,inorder)
    
    def getTree(self,preorder,inorder):
        if inorder:
            idx = inorder.index(preorder.popleft())
            root = TreeNode(inorder[idx])
            root.left = self.getTree(preorder,inorder[:idx])
            root.right = self.getTree(preorder,inorder[idx+1:])
            return root

# @lc code=end

