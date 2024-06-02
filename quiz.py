
def reverse_list(l : list):
    length = len(l)
    if length <= 1:
        return l
    else:
        reversed_out = reverse_list(l[1:-1])
        return [l[-1]] + reversed_out + [l[0]] if l[-1] != l[0] else reversed_out + l[0]
    
    pass
    

##### solve_sudoku ######
def is_valid(matrix, row, col, num):  
    # row check  
    
    for i in range(9):  
        if matrix[row][i] == num:  
            return False 
         
    # column check  
    for i in range(9):  
        if matrix[i][col] == num:  
            return False
          
    # every 3*3 grid check 
    start_row = row - row % 3  
    start_col = col - col % 3  
    for i in range(3):  
        for j in range(3):  
            if matrix[i + start_row][j + start_col] == num:  
                return False  
    return True 


def solve_sudoku(matrix):  
    for i in range(9):  
        for j in range(9):  
            if matrix[i][j] == 0:  
                for num in range(1, 10):  
                    if is_valid(matrix, i, j, num):  
                        matrix[i][j] = num  
                        if solve_sudoku(matrix):  
                            return True  
                        # recall if the number cannot meet the sudoku requirements  
                        matrix[i][j] = 0  
                return False  # If the number cannot be found, then this cell has no solution and will be traced back to the previous blank 
    return matrix  # return the solution
    
    