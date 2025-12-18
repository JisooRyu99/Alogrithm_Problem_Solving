# 1
class Solution:
    def check1(self, lines):
        nums = [n for n in lines if n.isdigit()]
        return len(list(set(nums))) == len(nums)
    

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for line in board:
            if not self.check1(line):
                return False
        
        vert = []
        for i in range(len(board)):
            tmp = []
            for j in range(len(board[0])):
                tmp.append(board[j][i])
            vert.append(tmp)  
        
        for line in vert:
            if not self.check1(line):
                return False
        
        Three = [[] for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                tmp_idx = (i//3) * 3 + (j//3)
                Three[tmp_idx].append(board[i][j])
        for line in Three:
            if not self.check1(line):
                return False
            
        return True


# 정답은 맞지만 너무 복잡
        
