class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        heights = heights + [0]

        for i, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                popped = stack.pop()

                rec_height = heights[popped]

                if stack:
                    rec_width = i - stack[-1] - 1
                else: 
                    rec_width = i

                max_area = max(max_area, rec_height * rec_width)

            stack.append(i)

        return max_area
        