class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row={i:[] for i in range(9)}
        col={i:[] for i in range(9)}
        box={(i,j):[] for i in range(3) for j in range(3)}

        for r in range(9):

            for c in range(9):
                
                if board[r][c] == ".":

                    continue
                
                else:

                    if board[r][c] not in row[r]:

                        row[r].append(board[r][c])
                    
                    else:

                        return False

                    if board[r][c] not in col[c]:

                        col[c].append(board[r][c])
                    
                    else:

                        return False  

                    if board[r][c] not in box[(r//3,c//3)]:

                        box[(r//3,c//3)].append(board[r][c])
                    
                    else:

                        return False       
        print("ROWS",row,"\n","COLS",col,"\n","BOXES",box)
        return True              
                


                
                


        