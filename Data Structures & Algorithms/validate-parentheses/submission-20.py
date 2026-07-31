class Solution:
    def isValid(self, s: str) -> bool:

        #an odd length means that there is a parenthesis without a pair
        #a marginal improvement O(N/c), only here to demonstrate understanding
        if len(s) % 2 == 1:
            return False
        
        stack = []

        openP = {'(':')',
                '[':']',
                '{':'}'}

        for l in s:
            
            #if l is an opening parenthesis
            #push an equilavent closed one on the stack
            if l in openP:
                stack.append(openP[l])
            #else check the stack for the closed one
            
            elif stack and stack[-1] == l:
                del stack[-1]
            else:
                return False

        #a successful run will remove all elements from the stack
        #since those elements must occur by necessity to create a valid entry
        return not stack




        