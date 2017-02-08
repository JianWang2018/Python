# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
#
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#
#
# A partially filled sudoku which is valid.
#
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

class Solution(object):
    def isValidSudoku(self, board):
        used1,used2,used3=[[0]*9 for _ in range(9)],[[0]*9 for _ in range(9)],[[0]*9 for _ in range(9)]

        for i in range(9):

            for j in range(9):
                if board[i][j]!=".":
                    k=int(i/3)*3+int(j/3)
                    num = int(board[i][j])-1
                    if used1[i][num] or used2[j][num] or used3[k][num]:
                        return False
                    used1[i][num]=used2[j][num]=used3[k][num]=1

        return True


def main():
    s=[".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
    sln=Solution().isValidSudoku(s)
    print(sln)

if __name__=="__main__":
    main()