class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #updated solution to use hashsets instead os lists
        row={i:set() for i in range(9)}
        col={i:set() for i in range(9)}
        box={(i,j):set() for i in range(3) for j in range(3)}

        for r in range(9):

            for c in range(9):
                
                if board[r][c] == ".":

                    continue
                
                else:

                    if board[r][c] not in row[r]:

                        row[r].add(board[r][c])
                    
                    else:

                        return False

                    if board[r][c] not in col[c]:

                        col[c].add(board[r][c])
                    
                    else:

                        return False  

                    if board[r][c] not in box[(r//3,c//3)]:

                        box[(r//3,c//3)].add(board[r][c])
                    
                    else:

                        return False       
        print("ROWS",row,"\n","COLS",col,"\n","BOXES",box)
        return True              
                


                
                


        