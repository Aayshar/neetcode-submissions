class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap={}
        
        for i,v in enumerate(numbers):
            if target-v in hashmap:
                return [hashmap[target-v]+1,i+1]
            else:
                hashmap[v]=i

        