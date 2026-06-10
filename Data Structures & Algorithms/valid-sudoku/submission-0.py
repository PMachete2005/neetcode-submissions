class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i = 0
        while i < 9:
            j = 0
            mySet = set()
            while j < 9:
                if board[i][j] != ".":
                    if board[i][j] in mySet:
                        return False
                    else:
                        mySet.add(board[i][j])
                j += 1
            i += 1
        k = 0
        while k < 9:
            l = 0
            mySet = set()
            while l < 9:
                if board[l][k] != ".":
                    if board[l][k] in mySet:
                        return False
                    else:
                        mySet.add(board[l][k])
                l += 1
            k += 1
        a = 0 
        while a < 9:
            b = (a // 3) * 3
            mySet = set()
            c = (a % 3) * 3
            cntrow = 0
            while cntrow < 3:
                cntcol = 0
                while cntcol < 3:
                    x = b + cntrow
                    y = c + cntcol
                    if board[x][y] != ".":
                        if board[x][y] in mySet:
                            return False
                        else:
                            mySet.add(board[x][y])
                    cntcol += 1
                cntrow += 1
            a += 1
        return True