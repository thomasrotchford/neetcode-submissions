class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #height,index
        stack = [(-1,-1)]

        heights.append(-1)
        sol = 0

        for i,h in enumerate(heights):

            while h < stack[-1][0]:
                col = stack.pop()
                area = col[0]*((i-1) - stack[-1][1])
                sol = max(sol,area)

            stack.append((h,i))

        return sol