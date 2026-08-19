class Solution:
    def maxArea(self, h: List[int]) -> int:
        res=0
        i=0
        j=len(h)-1
        while i<j:
             cap=min(h[i],h[j])*(j-i)
             res=max(res,cap)
             if h[i]<h[j]:
                 i+=1
             else:
                j-=1
        return res