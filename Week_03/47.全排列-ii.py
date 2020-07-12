#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l)+1):
                    new_ans.append(l[:i]+[n]+l[i:])
                    if i<len(l) and l[i]==n:
                        break      
            ans = new_ans
        return ans
# @lc code=end

