class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        memo = {}
        res = 0
        index = 0
        for i in nums:
            if i not in memo:
                res += 1
                memo[i] = 1
                nums[index] = i
                index += 1

        return res
