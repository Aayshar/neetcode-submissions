class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1={}
        count2={}
        if len(s1)>len(s2):
            return False
        for ch in s1:
            if ch in count1:
                count1[ch]+=1
            else:
                count1[ch]=1
        for i in range(len(s1)):
            if s2[i] in count2:
                count2[s2[i]]+=1
            else:
                count2[s2[i]]=1
        if count1==count2:
            return True
        left=0
        for right in range(len(s1),len(s2)):
            if s2[right] in count2:
                count2[s2[right]]+=1
            else:
                count2[s2[right]]=1
            count2[s2[left]]-=1
            if count2[s2[left]]==0:
                del count2[s2[left]]
            left+=1

            if count1==count2:
                return True
        return False


