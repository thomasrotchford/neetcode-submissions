class Solution: #helped used, reccomended time complexity and topics
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l = 0
        
        #subString's Characteristic
        subChar = defaultdict(int)
        lazyRefactor = defaultdict(int)
        subChar
        for c in s1:
            #count,firstseeninscopestack
            if c not in subChar:
                subChar[c]=[1,[]]
            else:
                subChar[c][0]+=1
            lazyRefactor[c]+=1
        #print(lazyRefactor)
        #solution's Characteristic
        buildChar = defaultdict(int)

        for r,v in enumerate(s2):
            
            if v in subChar:

                buildChar[v]+=1

                #else if char exceeds amount that should exist
                #print(buildChar[v],subChar[v])
                #print(v)
                if buildChar[v] > subChar[v][0]:
                    
                    for i in range(l, subChar[v][1][0]+1):
                        #decrement all values falling out of scope including the last seen index
                        if buildChar[s2[i]] and buildChar[s2[i]] > 0:
                            #print(buildChar[s2[i]])
                            buildChar[s2[i]]-= 1

                    #bump l to 1+ that spot
                    subChar[v][1].append(r)
                    l = subChar[v][1].pop(0)+1
                    
                else: 
                    #update firstseeninscopeindex
                    subChar[v][1].append(r)

            else:
                #reset buildChar 
                buildChar.clear()

                #skip index
                l = r + 1
                 
            #if characteristics are the same return True
            #print(s2[l:r+1])

            #print(buildChar)
            if buildChar == lazyRefactor:
                return True



        return False