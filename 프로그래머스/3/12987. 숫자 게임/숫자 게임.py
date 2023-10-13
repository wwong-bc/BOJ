def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    win = 0
    for b in B:
        for a in A:
            if a < b:
                win += 1
                A.pop(A.index(a))
                break
    return win
    