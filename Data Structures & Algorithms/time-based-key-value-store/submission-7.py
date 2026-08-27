class TimeMap:

    def __init__(self):
        self.d = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.d:
            self.d[key] = [[value],[timestamp]]
        else:
            self.d[key][0].append(value)
            self.d[key][1].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:

        if key in self.d:
            stamps = self.d[key][1]
            vals = self.d[key][0]
            l = 0
            r = len(stamps)-1
            sol = -1

            while l <= r:
                m=((r-l)//2)+l

                if stamps[m] == timestamp:
                    return vals[m]
                elif stamps[m] < timestamp:
                    sol = m
                    l = m+1
                else:
                    r = m-1
            return vals[sol] if sol != -1 else ""


        return ""
        