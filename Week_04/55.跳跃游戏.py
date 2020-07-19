#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp=[False]*len(nums)
        dp[-1]=True
        index=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if index-i<=nums[i]:
                index=i
                dp[index]=True
        
        return dp[0]



# @lc code=end

