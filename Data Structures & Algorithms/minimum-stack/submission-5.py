class MinStack:

    def __init__(self):
        self.stack=[]
        self.mFlag=0

    def push(self, val: int) -> None:

        diff=val-self.mFlag
        #if stack empty
        if not self.stack:
            self.stack.append(0)
            self.mFlag=val
        #if new min is found
        elif diff<0:
            self.stack.append(diff)
            self.mFlag=val
        #if adding new non-min value
        else:
            self.stack.append(diff)
        

    def pop(self) -> None:

        #if top is min
        if self.stack[-1]<0:
            #set flag to previous min
            self.mFlag=self.mFlag-self.stack[-1]

        #if top is not min
        del self.stack[-1]

    def top(self) -> int:
        
        #if top is min
        if self.stack[-1]<0:
            return self.mFlag
        #if top is not min
        else:
            return self.stack[-1]+self.mFlag

        

    def getMin(self) -> int:
        return self.mFlag
        
