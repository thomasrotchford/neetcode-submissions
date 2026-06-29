class MinStack:

    def __init__(self):
        self.stack=[]
        self.length=0
        

    def push(self, val: int) -> None:
        
        self.length+=1
        self.stack.append(val)


    def pop(self) -> None:

        del self.stack[self.length-1]
        self.length-=1

    def top(self) -> int:
        return(self.stack[self.length-1])

    def getMin(self) -> int:
        return min(self.stack)
        
