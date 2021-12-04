'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

'''


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # each row contains non repeated 1-9
        # each column contains not repeated 1-9
        col_len = len(board)
        row_len = len(board[1])
        row_sets = set()
        col_sets = set()
        for i in range(col_len):
            for j in range(row_len):
                s1 = board[i][j]
                s2 = board[j][i]
                if s1 == '.' or s2 == '.':
                    break
                s1_int = int(s1)
                s2_int = int(s2)
                if s1 in row_sets or s1_int >9 or s1_int<0:
                    return False
                else:
                    row_sets.add(s1)

                if s2 in col_sets or s2_int >9 or s2_int < 0:
                    return False
                else:
                    col_sets.add(s2)
            row_sets ={}
            col_sets ={}

        return True








s = Solution()
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(s.isValidSudoku(board))