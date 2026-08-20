class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        checkRow = [set([]),set([]),set([]),set([]),set([]),set([]),set([]),set([]),set([])]
        checkCol = [set([]),set([]),set([]),set([]),set([]),set([]),set([]),set([]),set([])]
        checkBox = [set([]),set([]),set([]),set([]),set([]),set([]),set([]),set([]),set([])]

        for r in range(len(board)):
            for c in range(len(board)):
                cell = board[r][c]

                if cell == ".":
                    continue
                
                if cell not in checkRow[r]:
                    checkRow[r].add(cell)
                else:
                    return False
                
                if cell not in checkCol[c]:
                    checkCol[c].add(cell)
                else:
                    return False

                if cell not in checkBox[(c//3)+(r//3)*3]:
                    checkBox[(c//3)+(r//3)*3].add(cell)
                else:
                    return False
                
        return True