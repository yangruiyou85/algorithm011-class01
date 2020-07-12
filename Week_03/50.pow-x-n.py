#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            return 1.0 / self.myPow(x,-n)
        self.half=self.myPow(x,n//2)
        if n%2==0:
            return self.half*self.half
        else:
            return self.half* self.half*x
# @lc code=end

