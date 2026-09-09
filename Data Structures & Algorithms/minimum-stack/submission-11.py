class MinStack:

    def __init__(self):
        self.stack = []
        self.diff = int()
        

    def push(self, val: int) -> None:

        if not self.stack:

            self.stack.append(0)
            self.diff = val
        
        elif val < self.diff:

            self.stack.append(val-self.diff)
            self.diff = val

        else:

            self.stack.append(val-self.diff)
        #print(self.stack,self.diff)
        



    def pop(self) -> None:
        
        if self.stack[-1] < 0:

            self.diff = self.diff-self.stack[-1]
            
        self.stack.pop()
        #print(self.stack,self.diff)


    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.diff
        else:
            return self.stack[-1] + self.diff


    def getMin(self) -> int:
        return self.diff

        

