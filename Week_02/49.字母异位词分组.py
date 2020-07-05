#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        v_dict=collections.defaultdict(list)
        for s in strs:
            v_dict["".join(sorted(s))].append(s)
        return list(v_dict.values())



# @lc code=end

