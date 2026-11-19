class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [[] for _ in range(9)]
        print(cols)
        for row in board:
            nums = [num for num in row if num != "."]
            if len(set(nums)) != len(nums):
                return(False)
            for i, num in enumerate(row):
                cols[i].append(num)
        for col in cols:
            nums = [num for num in col if num != "."]
            if len(set(nums)) != len(nums):
                return(False)
        for i in range(0, 6, 3):
            for j in range(0, 6, 3):
                rows = board[i: i + 3]
                nums = []
                for row in rows:
                    nums += row[j: j + 3]
                nums = [num for num in nums if num != "."]
                if len(set(nums)) != len(nums):
                    return(False)
        return(True)
            
            