class TimeMap:
    #second time solving, aiming to improve based on feedback from yesterday while also not looking at previous notes or solution
    def __init__(self):
        self.d = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key in self.d:
            self.d[key][0].append(timestamp)
            self.d[key][1].append(value)
        else:
            self.d[key] = [[timestamp],[value]]

    def get(self, key: str, timestamp: int) -> str:
        
        #case: search for non existant key or in non initialized object
        if key not in self.d or not self.d:
           return "" 

        searchArr = self.d[key][0]

        l = 0
        r = len(searchArr)-1

        solution = -1
        while l <= r:
            m = ((r-l)//2)+l

            if searchArr[m] <= timestamp:
                solution = m
                l = m+1
            elif searchArr[m] > timestamp:
                r = m-1
        
        #case: d exists in k but there are no timestamps <= the target
        return self.d[key][1][solution] if solution != -1 else ""
