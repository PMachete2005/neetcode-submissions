class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        a = 0 
        mySet = set()
        while a < 9:
            b = 0
            while b < 9:
                if board[a][b] != ".":
                    if board[a][b] in mySet:
                        return False
                    else:
                        mySet.add(board[a][b])
                b += 1
            a += 1
            mySet.clear()
        i = 0
        while i < 9:
            j = 0 
            while j < 9:
                if board[j][i] != ".":
                    if board[j][i] in mySet:
                        return False
                    else:
                        mySet.add(board[j][i])
                j += 1
            i += 1
            mySet.clear()
        cntr = 0
        while cntr < 9:
            row = 0
            col = 0
            if cntr != 0:
                row = (cntr // 3) * 3
                col = (cntr % 3) * 3
            cntrA = 0
            while cntrA < 3:
                cntrB = 0
                while cntrB < 3:
                    if board[row + cntrA][col + cntrB] != ".":
                        if board[row + cntrA][col + cntrB] in mySet:
                            return False
                        else:
                            mySet.add(board[row + cntrA][col + cntrB])
                    cntrB += 1
                cntrA += 1
            cntr += 1
            mySet.clear()
        return True

         

            


        
