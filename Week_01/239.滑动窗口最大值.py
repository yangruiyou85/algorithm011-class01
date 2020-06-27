#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        if not nums or k==0:
            return []
        n=len(nums)
        m=max(nums[:k])
        result=[m]
        for i in range(1,n-k+1):
            if nums[i-1]==m:
                m=max(nums[i:i+k])
            else:
                m=max(m,nums[i+k-1])
            result.append(m)
        return result
# @lc code=end

