class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # 0  1  2  3
        # 4  5  6  7
        # 8  9  10 11

        def calcPos(x1, x2, row, col):

            return (x1 * col) + x2

        def reversePos(X, row, col):

            r2 = 0
            c2 = 0

            while X >= col:

                X-=col
                r2+=1

            c2 = X

            return r2, c2


        l1, l2 = 0, 0

        row, col = len(matrix), len(matrix[0])

        r1, r2 = row-1, col-1

        L, R = 0, calcPos(r1,r2,row,col)

        print(row,col,'\n')


        while L <= R:



            L = calcPos(l1,l2,row,col)

            R = calcPos(r1,r2,row,col)

            M = ((R-L)//2)+L

            m1, m2 = reversePos(M,row,col)

            print(l1, l2, r1, r2)

            print(L, M, R)

            print(m1, m2)

            print('\n')

            if matrix[m1][m2] < target:

                l1, l2 = reversePos(M+1,row,col)

            elif matrix[m1][m2] > target:

                r1, r2 = reversePos(M-1,row,col)


            else: 

                return True

        return False
