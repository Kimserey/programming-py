class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, i in enumerate(nums):
            if i in map:
                return [map[i], index]
            else:
                remain = target - i
                map[remain] = index

        return []
