def solution(n):
    answer = 0
    index = 0
    i = 0
    while index < n:
        i+=1
        if i % 3 == 0 or "3" in str(i):
            continue
        index += 1        
    return i