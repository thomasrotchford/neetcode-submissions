class TimeMap:

    def __init__(self):
        self.d = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.d:
            self.d[key][0].append(timestamp)
            self.d[key][1][timestamp] = value
        else:
            self.d[key] = [[timestamp],{timestamp:value}]
        
    def get(self, key: str, timestamp: int) -> str:
        if key in self.d:
            searchArr = self.d[key][0]
            stampDict = self.d[key][1]
        else:
            return ""
        searchedStamp = -1
        l = 0
        r = len(searchArr)-1
        #print("looking for : ",timestamp)
        #print(searchArr)
        while l<=r:
            m = ((r-l)//2)+l
            #print(searchedStamp,l,m,r)
            if searchArr[m] <= timestamp:
                l=m+1
                searchedStamp = searchArr[m]
            elif searchArr[m] > timestamp:
                r=m-1
            else:
                searchedStamp = searchArr[m]
                break

        return stampDict[searchedStamp] if searchedStamp > -1 else ""
