class Solution:
    def threeSum(self, nums): 
        result = set()

        for i in range(len(nums)):
            seen = set()

            for j in range(i + 1, len(nums)):
                required = -(nums[i] + nums[j])

                if required in seen:
                    triplet = tuple(sorted([nums[i], nums[j], required]))
                    result.add(triplet)

                seen.add(nums[j])

        return [list(x) for x in result]