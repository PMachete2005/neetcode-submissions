class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #First we check row by row
        a = 0 
        while a < 9:
            mySet = set()
            b = 0
            while b < 9:
                if board[a][b] != ".":
                    if board[a][b] in mySet:
                        return False
                    else:
                        mySet.add(board[a][b])
                b += 1
            a += 1
        print("No row repeats")
        #Now we check column by column 
        i = 0
        while i < 9:
            mySet = set()
            j = 0 
            while j < 9:
                if board[j][i] != ".":
                    if board[j][i] in mySet:
                        return False
                    else:
                        mySet.add(board[j][i])
                j += 1
            i += 1
        print("No column repeats")
        #Now the more complicated box check:
        cntr = 0
        while cntr < 9:
            mySet = set()
            row = 0
            col = 0
            if cntr != 0:
                row = (cntr // 3) * 3
                col = (cntr % 3) * 3
            cntrA = 0
            while cntrA < 3:
                cntrB = 0
                while cntrB < 3:
                    print("Going to check:", row, col, "with counter", cntrA, cntrB)
                    if board[row + cntrA][col + cntrB] != ".":
                        if board[row + cntrA][col + cntrB] in mySet:
                            return False
                        else:
                            mySet.add(board[row + cntrA][col + cntrB])
                    cntrB += 1
                cntrA += 1
            cntr += 1
        return True

         

            


        
