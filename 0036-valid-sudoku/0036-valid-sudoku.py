class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        lrow=[]
        lbox=[]
        for i in range(9):
            for j in range(9):
                a=board[i][j]
                if a.isdigit()==False:
                    continue
                else:
                    if a in lrow:
                        return False
                    else:
                        lrow.append(a)    
            lrow.clear()

        for i in range(9):
            for j in range(9):
                a=board[j][i]
                if a.isdigit()==False:
                    continue
                else:
                    if a in lrow:
                        return False
                    else:
                        lrow.append(a)    
            lrow.clear()  

        for i in range(0,9,3):
            for j in range(0,9,3):
                for z in range(i,i+3):
                    for x in range(j,j+3):
                        a=board[z][x]
                        if a.isdigit()==False:
                            continue
                        else:
                            if a in lrow:
                                return False
                            else:
                                lrow.append(a)    
                lrow.clear()
            
        return True        