#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits):
        return list(map(int, list(str(int(''.join(map(str, digits))) + 1))))

# @lc code=end

