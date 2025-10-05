class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)
      
        # Stack to maintain indices of bars in increasing height order
        stack = []
      

        left_boundaries = [-1] * n

        right_boundaries = [n] * n
      

        for i, current_height in enumerate(heights):

            while stack and heights[stack[-1]] >= current_height:
                right_boundaries[stack[-1]] = i
                stack.pop()
          

            if stack:
                left_boundaries[i] = stack[-1]

            stack.append(i)
      
        max_area = max(
            height * (right_boundaries[i] - left_boundaries[i] - 1) 
            for i, height in enumerate(heights)
        )
      
        return max_area
