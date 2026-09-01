class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row, col= len(matrix), len(matrix[0])
        self.prefixsum = [[0]*col for i in range(row)]
        for i in range(row):
            self.prefixsum[i][0]=matrix[i][0]
            for j in range(1,col):
                self.prefixsum[i][j]= self.prefixsum[i][j-1] + matrix[i][j]

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res=0
        for row in range(row1, row2+1):
            if col1>0:
                res+= self.prefixsum[row][col2]-self.prefixsum[row][col1-1]
            else:
                res+= self.prefixsum[row][col2]
        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)