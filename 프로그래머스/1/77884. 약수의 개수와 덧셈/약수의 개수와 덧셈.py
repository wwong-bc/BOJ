def solution(left, right):
    answer = (left+right) * (right-left+1) / 2
    for i in range(32):
        temp = i * i
        if temp < left:
            continue
        elif temp > right:
            continue
        else:
            answer -= 2 * temp
    return answer