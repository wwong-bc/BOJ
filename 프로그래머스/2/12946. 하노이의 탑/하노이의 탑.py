def solution(n):
    answer = hanoi(1, 2, 3, n)
    return answer

def hanoi(start, middle, end, n):
    if n == 1:
        return [[start, end]]
    else:
        return hanoi(start, end, middle, n-1) + [[start, end]] + hanoi(middle, start, end, n-1)
