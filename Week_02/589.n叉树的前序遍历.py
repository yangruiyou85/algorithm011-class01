#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack ,res = [root,],[]
        while  stack:
            root=stack.pop()
            res.append(root.val)
            stack.extend(root.children[::-1])
        return res

        
# @lc code=end

