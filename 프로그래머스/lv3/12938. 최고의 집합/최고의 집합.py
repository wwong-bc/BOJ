def solution(n, s):
    if n > s:
        return [-1]
    else:
        q = s // n
        r = s % n
        answer = [q for _ in range(n)]
        for i in range(r):
            answer[i] += 1
        return sorted(answer)