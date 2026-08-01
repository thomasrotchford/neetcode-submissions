class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        #new problem
        #no resources used yet
        stack = []
        
        for token in tokens:
            print(stack)
            match token:

                case '+':
                    stack[-2]+=stack[-1]
                    del stack[-1]
                
                case '-':
                    stack[-2]-=stack[-1]
                    del stack[-1]

                case '*':
                    stack[-2]*=stack[-1]
                    del stack[-1]

                case '/':
                    stack[-2]= int(stack[-2] / stack[-1])
                    del stack[-1]

                case _:
                
                    stack.append(int(token))

        return stack[0]

        