#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def generate(S,permutation=[]):
            if S:
                for s in S:
                    yield from generate(S-{s}, permutation + [s])
            else:
                yield permutation
        return [*generate(set(nums))]  
# @lc code=end

