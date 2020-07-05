#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ntopNumer=collections.Counter(nums)
        return [ item[0] for item in ntopNumer.most_common(k)]
# @lc code=end

