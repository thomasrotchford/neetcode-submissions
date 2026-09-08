class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # (value,index)
        stack = [(-1,-1)]
        sol = 0

        #add minimum possible tail to cause stack to be popped
        heights.append(-1)

        for i,h in enumerate(heights):
            #print(stack)
            while h < stack[-1][0]:
                popped = stack.pop()
                width = i-stack[-1][1]-1
                sol = max(sol,width*popped[0])
                #print("the size of ",popped," is ",width*popped[0])
            
            stack.append((h,i))
        
        return sol