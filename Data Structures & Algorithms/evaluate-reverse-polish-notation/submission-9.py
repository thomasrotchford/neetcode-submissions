class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:

            match token:

                case "+":
                    stack.append(stack.pop(-1) + stack.pop(-1))
                case "-":
                    stack.append(stack.pop(-2) - stack.pop(-1))
                case "*":
                    stack.append(stack.pop(-1) * stack.pop(-1))
                case "/":
                    stack.append(int(stack.pop(-2) / stack.pop(-1)))
                case _:
                    stack.append(int(token))
            #print(stack)
        return stack.pop(-1)