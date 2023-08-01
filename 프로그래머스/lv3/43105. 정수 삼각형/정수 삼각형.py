def solution(triangle):
    height = len(triangle)
    new_triangle = []
    for i in range(height):
        if i == 0:
            new_triangle.append([triangle[0][0]])
            continue
        new_row = []
        for j in range(i+1):
            if j == 0:
                new_row.append(new_triangle[i-1][j] + triangle[i][j]) 
            elif j == i:
                new_row.append(new_triangle[i-1][j-1] + triangle[i][j])
            else:
                new_row.append(max(new_triangle[i-1][j-1], new_triangle[i-1][j]) + triangle[i][j])
        new_triangle.append(new_row)
    return max(new_triangle[-1])