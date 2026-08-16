class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        n=len(nums)
    
        nums.sort()
        res=[nums[0]]
        max_len=1
        for i in range(len(nums)-1 ):
            if nums[i]+1==nums[i+1]:
                res.append(nums[i+1])
            elif nums[i]!=nums[i+1]:
                max_len=max(max_len,len(res))
                res=[nums[i+1]]
        return max(max_len,len(res))
      