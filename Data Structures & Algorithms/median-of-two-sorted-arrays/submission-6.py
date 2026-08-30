class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums1len = len(nums1)
        nums2len = len(nums2)
        #calc theoretical spaces before median
        spacesBeforeMedian = (nums1len+nums2len)//2

        #make sure smaller array is nums1
        if nums1len > nums2len:
            temp = nums1
            nums1 = nums2
            nums2 = temp
            temp = nums1len
            nums1len = nums2len
            nums2len = temp

        #init loop
        l = 0
        r = nums1len #important edge case: r1 must ne able to go out of bounds to properly represent spaces before div

        while l <= r:
            #create dividers
            div1 = (l+r)//2
            r1 = div1
            l1 = div1-1

            div2 = spacesBeforeMedian - div1
            r2 = div2
            l2 = div2-1
            #[[value],[membership]]
            larray = [[],[]]
            rarray = [[],[]]

            #priming main comparision
            if -1 < l1 < nums1len:
                larray[0].append(nums1[l1])
                larray[1].append(1)
            if -1 < l2 < nums2len:
                larray[0].append(nums2[l2])
                larray[1].append(2)
            if -1 < r1 < nums1len:
                rarray[0].append(nums1[r1])
                rarray[1].append(1)
            if -1 < r2 < nums2len:
                rarray[0].append(nums2[r2])
                rarray[1].append(2)

            maxL = max(larray[0] if larray[0] else [float("-inf")])
            minR = min(rarray[0] if rarray[0] else [float("inf")])

            if maxL <= minR:
                #solve for solution
                parity = (nums1len+nums2len)%2

                if parity:
                    return minR
                else:
                    return (minR+maxL)/2

            else:
                if larray[1][0]==1 and (2 in rarray[1]) and nums1[l1] > nums2[r2]:
                    #too far right
                    r = div1-1

                else:
                    #too far left
                    l=div1+1




        