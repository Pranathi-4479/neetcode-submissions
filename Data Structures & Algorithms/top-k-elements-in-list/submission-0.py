class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_set={}
        l=[]
        for i in nums:
            if i in hash_set:
                hash_set[i]+=1
            else:
                hash_set[i]=1
        pairs=[]
        for _ in range(k):
            v=max(hash_set,key=hash_set.get)
            pairs.append(v)
            hash_set.pop(v)
        return pairs    