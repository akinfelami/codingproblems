def diagonalDifference(arr):
    right_sum = 0
    left_sum = 0
    col_left = 0
    col_right = len(arr[0])-1 # square matrix
    row = 0
    while row < len(arr):
        right_sum += arr[row][col_left]
        left_sum += arr[row][col_right]
        row +=1
        col_left+=1
        col_right-=1
        
    abs_diff  = abs(right_sum-left_sum)
    return abs_diff