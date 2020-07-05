#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if not root:
            return []
        queue = [(root, 0)]
        res = [[]]
        while queue:
            node, level = queue.pop(0)
            if level >= len(res):
                res.append([])
            res[level].append(node.val)
            for child in node.children:
                queue.append((child, level + 1))
        return res
     
# @lc code=end

