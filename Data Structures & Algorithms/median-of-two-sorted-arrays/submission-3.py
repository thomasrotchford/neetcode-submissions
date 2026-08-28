class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def answer(totalParity,nums1,nums2,after1,after2,before1,before2)->float:
            beforeArr = []
            afterArr = []
            if before1 > -1:
                beforeArr.append(nums1[before1])
            if before2 > -1:
                beforeArr.append(nums2[before2])
            if after1 < len(nums1):
                afterArr.append(nums1[after1])
            if after2 < len(nums2):
                afterArr.append(nums2[after2])

            if totalParity:
                    return min(afterArr)
            else:
                rightMedian = min(afterArr)     
                leftMedian = max(beforeArr)      
                return (rightMedian+leftMedian)/2

        mLen = len(nums1)
        nLen = len(nums2)
        #spaces before solution
        before = (mLen+nLen)//2

        #parity of sum of lengths
        totalParity = bool((mLen+nLen)%2)

        #handle edge case one subarray is empty
        if not nums1:
            if totalParity:
                return float(nums2[before])
            else:
                return float((nums2[before-1]+nums2[before])/2)

        elif not nums2:
            if totalParity:
                return float(nums1[before])
            else:
                return float((nums1[before-1]+nums1[before])/2)

        #find shorter array       
        if mLen > nLen:
            temp = nums2
            nums2 = nums1
            nums1 = temp
            mLen = len(nums1)
            nLen = len(nums2)

        l = 0
        r = mLen #edge case [1] [2,3] removed -1 div1 must be able to be [|1] and [1|]
        #poop=0
        print("BEFORE = ",before)
        print(mLen, " len ",nums1)
        print(nLen, " len ",nums2)
        while l<=r :
            div1 = (r+l)//2 
            after1 = div1 
            before1 = div1-1

            div2 = before-div1
            after2 = div2 
            before2 = div2-1
            print("LEFT = ",l)
            print("RIGHT = ",r)
            print(before1,after1)
            print(before2,after2)
            if div1>0 and div2>0:
                print("CASE 1")
                #3 subcases
                if after1 >= mLen:
                    if nums1[before1] > nums2[after2]:
                        r = before1 +1

                    else:
                        #solution found
                        print("1 FOUND")
                        return answer(totalParity,nums1,nums2,after1,after2,before1,before2)

                elif after2 >= nLen:
                    if nums2[before2] > nums1[after1]:
                        l = after1 +1

                    else:
                        #solution found
                        print("2 FOUND")
                        return answer(totalParity,nums1,nums2,after1,after2,before1,before2)
                
                else:

                    if max(nums1[before1], nums2[before2]) <= min(nums1[after1], nums2[after2]):
                        #solution found
                        print("3 FOUND")
                        return answer(totalParity,nums1,nums2,after1,after2,before1,before2)

                    elif nums1[before1] > nums2[after2]:
                        r = before1 +1

                    elif nums2[before2] > nums1[after1]:
                        l = after1 +1
            
            elif div1 == before:
                print("CASE 2")
                #2 subcases
                if after1 >= mLen and before2 < 0:
                    #solution found
                    print("5 FOUND")
                    return answer(totalParity,nums1,nums2,after1,after2,before1,before2)

                else: #before2 < 0
                    if nums1[before1] > nums2[after2]:
                        r = before1 +1
                    else:
                        print("6 FOUND")
                        return answer(totalParity,nums1,nums2,after1,after2,before1,before2)

            elif div2 == before:
                print("CASE 3")
                #2 subcases
                if after2 >= nLen and before1 < 0:
                    #solution found
                    print("7 FOUND")
                    return answer(totalParity,nums1,nums2,after1,after2,before1,before2)

                else: #before1 < 0
                    if nums2[before2] > nums1[after1]:
                        l = after1 +1

                    else:
                        print("8 FOUND")
                        return answer(totalParity,nums1,nums2,after1,after2,before1,before2)
            #poop+=1

            #check validity
            #if max() <= min()

            #if before1 > after2 div1 is too far right

            #elif before2 > after1 div1 is too far left


                

            










