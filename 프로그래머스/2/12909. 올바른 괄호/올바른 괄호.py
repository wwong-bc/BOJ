
def solution(s):
    a = 0
    for c in s:
        if c == "(":
            a += 1
        if c == ")":
            if a <= 0:
                return False
            a-= 1
    if a == 0:
        return True
    else:
        return False