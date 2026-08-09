class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_set={}
        for i,val in enumerate(nums):
            diff=target-nums[i]
            if diff in hash_set:
                return sorted([hash_set[diff], i])
            hash_set[val]=i