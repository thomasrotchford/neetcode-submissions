class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        l=0
        r=len(nums)-1

        while l<=r:
            
            m=((r-l)//2)+l

            if nums[m] == target:
                print("target in middle of subarray "+str(l)+" to "+str(r))
                return True

            #left half
            if nums[l] < nums[m]:
                print("left sorted from "+str(l)+" to "+str(m-1))
                # target in sorted?
                if nums[l] <= target <= nums[m]:
                    print(" target in left")
                    r=m-1
                else:
                    print(" target not in left")
                    l=m+1

            #right half
            elif nums[r] > nums[m]:
                print("right half sorted from "+str(m+1)+" to "+str(r))
                #target in sorted?
                if nums[m] <= target <= nums[r]:
                    print(" target in right half")
                    l=m+1
                else:
                    print(" target not in right half")
                    r=m-1
            #l==m==r or l==m or m==r 
            else:
                
                if nums[l]==nums[m]:
                    print("duplicate values on points: "+str(l)+" and "+str(m))
                    l+=1
                elif nums[m]==nums[r]:
                    print("duplicate values on points: "+str(m)+" and "+str(r))
                    r-=1
        

        return False