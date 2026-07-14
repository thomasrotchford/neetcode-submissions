class MinStack:

    #review

    def __init__(self):

        self.stack=[]

        self.min=0
        

    def push(self, val: int) -> None:



        if not self.stack :

            self.min = val 
            self.stack.append(val - self.min) 
        
              
        elif val - self.min < 0:

            self.stack.append(val - self.min) 
            self.min = val
        
        else:
            self.stack.append(val - self.min) 
            

    def pop(self) -> None:

        if self.stack[-1] < 0:

            self.min = (self.stack[-1] - self.min) * -1

        del self.stack[-1]
        

    def top(self) -> int:
        
        if self.stack[-1] < 0:

            return self.min

        else:
            
            return self.stack[-1] + self.min


    def getMin(self) -> int:

        return self.min

        
