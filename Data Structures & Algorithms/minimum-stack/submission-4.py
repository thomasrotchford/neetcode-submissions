class MinStack:
    #1,2,0
    #[1] m=1
    #[1,1] m=1
    #[1,1,-1] m=0

    def __init__(self):
        self.stack=[]
        self.m=0
        

    def push(self, val: int) -> None:

        if not self.stack:
            self.stack.append(0)
            self.m=val
        else:
            self.stack.append(val-self.m)
            if val<self.m:
                self.m=val

        
    #always called on non-empty stack
    def pop(self) -> None:

        if self.stack[len(self.stack)-1] < 0:
            self.m = self.m - self.stack[-1]
        if len(self.stack) == 1:
            self.m = 0
        del self.stack[-1]

        

    def top(self) -> int:

        if self.stack[-1]>0:

            return self.stack[-1]+self.m
        else:
            return self.m

        
        

    def getMin(self) -> int:

        return self.m
        
