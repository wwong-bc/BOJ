def solution(n):
    triangles = []
    for i in range(n):
        triangles.append([0 for _ in range(i+1)])

    full_number = int(n * (n+1) / 2)
    x = 0
    y = 0
    direction = 0
    for i in range(1, full_number+1):
        triangles[y][x] = i
        if direction == 0:
            if y == n-1:
                direction = 1
                x += 1
                continue
            if triangles[y+1][x]:
                direction = 1
                x += 1
                continue
            y += 1
        if direction == 1:
            if x == n-1:
                direction = 2
                x -= 1
                y -= 1
                continue
            if triangles[y][x+1]:
                direction = 2
                x -= 1
                y -= 1
                continue
            x += 1    
        if direction == 2:
            if triangles[y-1][x-1]:
                direction = 0
                y += 1
                continue
            y -= 1
            x -= 1
    answer = []
    for piece in triangles:
        answer += piece

    return answer