class Solution:
    def isValid(self, s: str) -> bool:

        stack = ["b"]

        parenthesis = {
            "[" : "]",
            "(" : ")",
            "{" : "}",
            "b" : "bottom"
        }
        
        for c in s:

            if c in parenthesis:
                stack.append(c)
            
            elif parenthesis[stack[-1]] == c:
                del stack[-1]
            
            else:
                return False
        
        return len(stack) == 1