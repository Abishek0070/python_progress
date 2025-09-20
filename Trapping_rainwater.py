class Solution(object):
    def trap(self, height):
        l, r = 0, len(height) - 1
        lMAX, rMAX = height[l], height[r]
        res = 0

        while l < r:
            if lMAX < rMAX:
                l += 1
                lMAX = max(lMAX, height[l])
                res += lMAX - height[l]
            else:
                r -= 1
                rMAX = max(rMAX, height[r])
                res += rMAX - height[r]
        
        return res
