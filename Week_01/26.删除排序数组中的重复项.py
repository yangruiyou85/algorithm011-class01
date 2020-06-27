#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for self.index in range(len(nums)-1,0,-1):
            if nums[self.index]==nums[self.index-1]:
                nums.pop(self.index)
        return len(nums)

# @lc code=end

