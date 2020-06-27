#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not 0 in nums:
            return
        self.i=0
        self.zeroNum=0
        while self.i <len(nums):
            if nums[self.i]==0:
                nums.pop(self.i)
                self.zeroNum+=1
            else:
                self.i+=1
        nums+=[0]*self.zeroNum


# @lc code=end

