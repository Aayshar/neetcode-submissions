class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1

        leftmost=0
        rightmost=0
        water=0

        while left<right:
            if height[left]<=height[right]:
                if height[left]>=leftmost:
                    leftmost=height[left]
                else:
                    water+=leftmost-height[left]
                left+=1
            else:
                if height[right]>=rightmost:
                    rightmost=height[right]
                else:
                    water+=rightmost-height[right]
                right-=1
        return water
                

        