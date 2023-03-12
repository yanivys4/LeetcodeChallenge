class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left,right = 0,len(height) - 1
        maxAreaFound = 0
        while left < right:
            leftHeight = height[left]
            rightHeight = height[right]
            area = min(leftHeight,rightHeight) * (right - left)
            maxAreaFound = max(area,maxAreaFound)
            if leftHeight < rightHeight:
                left += 1
            else:
                right -= 1
        return maxAreaFound
