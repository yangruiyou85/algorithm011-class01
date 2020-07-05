#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        stack=[]
        result=[]
        while root or len(stack) >0:
            if root:
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                result.append(root.val)
                root=root.right
        return result

# @lc code=end

