# Trapping Rain water problem (using two pointers approach)

class Solution:
  def trap(self, height: List[int]) -> int:
    
    if not height: retun 0
      
    left, right = 0, len(height) - 1
    leftMax, rightMax = height[1], height[r]
    res = 0
    
    while left < right:
      if leftMax < rightMax:
        left += 1
        leftMax = max(leftMax, height[left])
        ans += leftMax - height[left]
      else:
        right -= 1
        rightMax = max(rightMax, height[r])
        ans += rightMax - height[right]
    return ans    
