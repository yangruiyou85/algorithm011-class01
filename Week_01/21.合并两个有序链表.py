#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 == None: 
            return l2
        if l2 == None: 
            return l1
        if l1.val<=l2.val:
            h = l1
            h.next = self.mergeTwoLists(l1.next, l2)
        else:
            h = l2
            h.next = self.mergeTwoLists(l1, l2.next)
        return h      
# @lc code=end

