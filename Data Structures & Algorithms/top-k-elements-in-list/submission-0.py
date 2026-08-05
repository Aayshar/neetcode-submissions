class Solution:
    def topKFrequent(self, nums: List[int], k: int) ->List[int]:
        hashmap={}
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        sorted_items=sorted(hashmap.items(),key=lambda x:x[1],reverse=True)
        ans=[]
        for i in range(k):
            ans.append(sorted_items[i][0])
        return ans
        