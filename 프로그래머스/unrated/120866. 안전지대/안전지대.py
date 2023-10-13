def solution(board):
    answer = 0
    n = len(board)
    for i in range(n):
        for j in range(n):
            answer += around_search(board, i, j, n)

    return answer


def around_search(array, x, y, n):
    dx = [-1, -1, -1, 0, 1, 0, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, -1, 0, -1, 0]
    for k in range(9):
        nx, ny = x + dx[k], y + dy[k]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if array[nx][ny] == 1:
            return 0
    return 1