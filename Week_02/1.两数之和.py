#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target):
        d = {}
        for x in range(len(nums)):
            if target - nums[x] in d:
                return d[target-nums[x]],x
            else:
                d[nums[x]] = x
    
# @lc code=end

