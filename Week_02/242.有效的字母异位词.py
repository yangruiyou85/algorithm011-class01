#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if sorted(s)==sorted(t) else False



# @lc code=end

